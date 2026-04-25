import bpy
import math
import re
from collections import defaultdict

# ─────────────────────────────────────────────
FINGER_PREFIXES = ["c_thumb", "c_index", "c_middle", "c_ring", "c_pinky"]
SIDES = [".l", ".r"]
Z_OFFSET = 0.02
Y_OFFSET = -0.02

EXCLUDE_SUBSTRINGS = ["_base", "_meta", "_root", "c_thumb0", "c_thumb1"]

ROLL_FINGERS = math.radians(284)
ROLL_THUMB = math.radians(309)


# ─────────────────────────────────────────────

def split_side(name: str):
    for side in SIDES:
        if name.lower().endswith(side):
            return name[: -len(side)], name[-len(side):]
    return name, None


def get_finger_prefix(base: str):
    lower = base.lower()
    for prefix in FINGER_PREFIXES:
        if prefix in lower:
            return prefix
    return None


def is_roll_bone(name: str) -> bool:
    return "_roll" in name.lower()


def is_finger_bone(name: str) -> bool:
    if is_roll_bone(name):
        return False
    base, side = split_side(name)
    if side is None:
        return False
    if get_finger_prefix(base) is None:
        return False
    lower_base = base.lower()
    if any(excl in lower_base for excl in EXCLUDE_SUBSTRINGS):
        return False
    return True


def is_thumb(name: str) -> bool:
    return "thumb" in name.lower()


def get_roll_for_bone(name: str) -> float:
    return ROLL_THUMB if is_thumb(name) else ROLL_FINGERS


def make_roll_name(original: str) -> str:
    base, side = split_side(original)
    if side:
        return base + "_roll" + side
    return original + "_roll"


def segment_key(name: str):
    base, _ = split_side(name)
    nums = re.findall(r'\d+', base)
    return int(nums[-1]) if nums else 0


def group_finger_bones(bone_names):
    groups = defaultdict(list)
    for name in bone_names:
        base, side = split_side(name)
        prefix = get_finger_prefix(base)
        if prefix and side:
            groups[(prefix, side.lower())].append(name)
    for key in groups:
        groups[key].sort(key=segment_key)
    return groups


def apply_offset(bone, name: str):
    if is_thumb(name):
        bone.head.y += Y_OFFSET
        bone.tail.y += Y_OFFSET
    else:
        bone.head.z += Z_OFFSET
        bone.tail.z += Z_OFFSET


# ─────────────────────────────────────────────
def run():
    obj = bpy.context.active_object
    if obj is None or obj.type != 'ARMATURE':
        raise RuntimeError("Select an Armature before running the script, dummy")

    arm = obj.data
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = arm.edit_bones

    # ── 1. gets root finger bones (without _base) ───────────────────────
    finger_names = [b.name for b in edit_bones if is_finger_bone(b.name)]

    if not finger_names:
        bpy.ops.object.mode_set(mode='POSE')
        raise RuntimeError(
            "No finger bone found :( "
            "Check if finger bones are named: c_thumb/c_index/c_middle/c_ring/c_pinky and finish with .l/.r"
        )

    groups = group_finger_bones(finger_names)

    print(f"\n[finger_bones_roll] Grupos detectados:")
    for (prefix, side), names in sorted(groups.items()):
        print(f"  ({prefix}, {side}): {names}")

    # ── 2. maps root → roll and creates edit_bones ───────────────────────────
    roll_map = {}
    created_order = []

    for (prefix, side), sorted_names in groups.items():
        for src_name in sorted_names:
            roll_name = make_roll_name(src_name)
            roll_map[src_name] = roll_name
            created_order.append((roll_name, src_name))

    for roll_name, src_name in created_order:
        if roll_name in edit_bones:
            print(f"  [skip] '{roll_name}' já existe.")
            continue

        src = edit_bones[src_name]
        new_bone = edit_bones.new(roll_name)

        new_bone.head = src.head.copy()
        new_bone.tail = src.tail.copy()
        new_bone.matrix = src.matrix.copy()
        new_bone.use_connect = False

        apply_offset(new_bone, roll_name)

        new_bone.roll = get_roll_for_bone(roll_name)

    # ── 3. parent fix  ─────────────────────────────────────
    #
    #   roll[0]  →  original[0]
    #   roll[i]  →  roll[i-1]
    #
    #   Thumb:
    #   c_thumb2_roll.l  →  c_thumb2.l
    #   c_thumb3_roll.l  →  c_thumb2_roll.l
    #
    for (prefix, side), sorted_names in groups.items():
        for i, src_name in enumerate(sorted_names):
            roll_name = roll_map[src_name]

            if roll_name not in edit_bones:
                continue

            roll_bone = edit_bones[roll_name]

            if i == 0:
                roll_bone.parent = edit_bones[src_name].parent
            else:
                prev_roll = roll_map[sorted_names[i - 1]]
                if prev_roll in edit_bones:
                    roll_bone.parent = edit_bones[prev_roll]

    # ── 4. fix root bones roll ──────────────────────────────────────────
    for name in finger_names:
        if name in edit_bones:
            edit_bones[name].roll = get_roll_for_bone(name)

    # ── 5. back to pose mode and locks transforms from roll[0] ─────────────
    bpy.ops.object.mode_set(mode='POSE')

    for (prefix, side), sorted_names in groups.items():
        first_roll_name = roll_map.get(sorted_names[0])
        if not first_roll_name:
            continue
        pb = obj.pose.bones.get(first_roll_name)
        if pb is None:
            continue

        pb.lock_location = (True, True, True)

        pb.lock_scale = (True, True, True)

        if is_thumb(first_roll_name):
            pb.lock_rotation = (False, True, True)
        else:
            pb.lock_rotation = (True, True, False)

    print(f"\n[finger_bones_roll] Parenting:")
    for (prefix, side), sorted_names in sorted(groups.items()):
        print(f"\n  [{prefix} {side}]")
        for i, src_name in enumerate(sorted_names):
            roll_name = roll_map[src_name]
            parent_label = src_name if i == 0 else roll_map[sorted_names[i - 1]]
            print(f"    {roll_name}  →  {parent_label}")

    # ── 6. copy rotation: roll[i] copies roll[i+1] ────────────────────────
    #
    #   c_index1_roll.l  →  copies c_index2_roll.l
    #   c_index2_roll.l  →  copies c_index3_roll.l

    for (prefix, side), sorted_names in groups.items():
        roll_chain = [roll_map[n] for n in sorted_names if roll_map.get(n) in obj.pose.bones]

        for i in range(1, len(roll_chain)):
            src_pb = obj.pose.bones[roll_chain[i]]
            tgt_name = roll_chain[i - 1]

            # Removes duplicate constraints
            for c in list(src_pb.constraints):
                if c.type == "COPY_ROTATION" and c.subtarget == tgt_name:
                    src_pb.constraints.remove(c)

            con = src_pb.constraints.new("COPY_ROTATION")
            con.target = obj
            con.subtarget = tgt_name
            con.mix_mode = "REPLACE"
            con.target_space = "LOCAL_OWNER_ORIENT"
            con.owner_space = "LOCAL"

    # ── 8. copy rotation: root copies _roll (Mix: Add) ────────
    #
    #   c_index1.l  →  copia de c_index1_roll.l   (Add)
    #   c_index2.l  →  copia de c_index2_roll.l   (Add)
    #   c_index3.l  →  copia de c_index3_roll.l   (Add)

    for (prefix, side), sorted_names in groups.items():
        for src_name in sorted_names:
            roll_name = roll_map.get(src_name)
            if not roll_name or src_name not in obj.pose.bones:
                continue

            pb = obj.pose.bones[src_name]

            # removes duplicates
            for c in list(pb.constraints):
                if c.type == "COPY_ROTATION" and c.subtarget == roll_name:
                    pb.constraints.remove(c)

            con = pb.constraints.new("COPY_ROTATION")
            con.target = obj
            con.subtarget = roll_name
            con.mix_mode = "ADD"
            con.target_space = "LOCAL_OWNER_ORIENT"
            con.owner_space = "LOCAL"

    # ── 9. hides _roll[1] e _roll[2]  ──────
    for (prefix, side), sorted_names in groups.items():
        roll_chain = [roll_map[n] for n in sorted_names if roll_map.get(n)]
        for bone_name in roll_chain[1:]:  # pula [0], esconde o resto
            pb = obj.pose.bones.get(bone_name)
            if pb:
                pb.hide = True

    # ── 10. bone widgets ────────────────────────────────

    bpy.ops.object.mode_set(mode='POSE')

    def assign_widget(pb, shape_name):
        bpy.ops.pose.select_all(action='DESELECT')
        pb.select = True
        obj.data.bones.active = pb.bone
        try:

            bpy.context.window_manager.widget_list = shape_name
            with bpy.context.temp_override(
                    active_object=obj,
                    object=obj,
                    active_pose_bone=pb,
                    selected_pose_bones=[pb],
            ):
                bpy.ops.bonewidget.create_widget()
            print(f"  [widget] '{pb.name}'  ←  {shape_name}")
        except Exception as e:
            print(f"  [widget] Error: '{pb.name}': {e}")

    for (prefix, side), sorted_names in groups.items():
        roll_chain = [roll_map[n] for n in sorted_names if roll_map.get(n) in obj.pose.bones]

        if not roll_chain:
            continue

        pb0 = obj.pose.bones[roll_chain[0]]
        assign_widget(pb0, "Sphere")

        if is_thumb(roll_chain[0]) and len(roll_chain) > 1:
            pb1 = obj.pose.bones[roll_chain[0]]
            assign_widget(pb1, "Arrow Double (straight)")

    for (prefix, side), sorted_names in groups.items():
        roll_chain = [roll_map[n] for n in sorted_names if roll_map.get(n) in obj.pose.bones]
        for roll_name in roll_chain:
            pb = obj.pose.bones[roll_name]
            pb.color.palette = 'THEME01'

    print(f"\n[finger_bones_roll] done")
    print(f"  Offset index/middle/ring/pinky  : Z +{Z_OFFSET}")
    print(f"  Offset thumb  : Y +{Y_OFFSET}")
    print(f"  Roll index/middle/ring/pinky : {math.degrees(ROLL_FINGERS):.0f}°")
    print(f"  Roll thumb                   : {math.degrees(ROLL_THUMB):.0f}°")
    print("the rig should be done, now please sedate me.")


run()