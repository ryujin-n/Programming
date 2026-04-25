import bpy
import math
import re
import pathlib
from collections import defaultdict

FINGER_PREFIXES = ["c_thumb", "c_index", "c_middle", "c_ring", "c_pinky"]
SIDES = [".l", ".r"]
Z_OFFSET = 0.02
Y_OFFSET = -0.02

EXCLUDE_SUBSTRINGS = ["_base", "_meta", "_root", "c_thumb0", "c_thumb1"]

ROLL_FINGERS = math.radians(284)
ROLL_THUMB = math.radians(309)

HAND_CONTROL_LEN      = 0.03
HAND_CONTROL_Z_OFFSET = 0.04
BONE_CONFIGS = [("_L", ".l", 1), ("_R", ".r", -1)]
BONE_BASE_NAME = "hand_control"

WIDGET_SHAPE = "Root 1"
WIDGET_ROT_X = math.radians(0)
WIDGET_ROT_Y = math.radians(90)
WIDGET_ROT_Z = math.radians(90)
WIDGET_WIRE_WIDTH = 2.00

# for now, please put the path for the actions.py, you can save it anywhere, just link the path inside the ""

ACTIONS_PATH = pathlib.Path(
    r""  #ex: r"C:\Users\...\Download\actions.py"
# YOU NEED TO POINT OUT THE actions.py FILE, OR IT WILL NOT WORK
)
OVERWRITE_EXISTING = False
USE_FAKE_USER = True


# ── Action Constraint Map ─────────────────────────────────────────────────────

def P(action, constraint, expr, ttype, rot_mode=None):
    return dict(action=action, constraint=constraint,
                expr=expr, type=ttype, rot_mode=rot_mode)


ACTION_CONSTRAINT_MAP = {
    ".l": {
        "ctrl": "hand_control_L",
        "groups": [
            {
                "bones": ["c_pinky1_roll", "c_ring1_roll", "c_middle1_roll", "c_index1_roll", "c_thumb2_roll"],
                "pairs": [
                    P("fist.l", "Action_fist.l", "max(0.0, min(1.0, var / -0.03))", "LOC_X"),
                    P("extend.l", "Action_extend.l", "max(0.0, min(1.0, var /  0.03))", "LOC_X"),
                ],
            },
            {
                "bones": ["c_thumb1"],
                "pairs": [
                    P("fist.l", "Action_fist.l", "max(0.0, min(1.0, var / -0.03))", "LOC_X"),
                    P("extend.l", "Action_extend.l", "max(0.0, min(1.0, var /  0.03))", "LOC_X"),
                    P("roll.l", "Action_roll.l", "max(0.0, min(1.0, var / -0.500))", "ROT_X", "QUATERNION"),
                    P("roll2.l", "Action_roll2.l", "max(0.0, min(1.0, var /  0.500))", "ROT_X", "QUATERNION"),
                    P("adduction.l", "Action_adduction.l", "max(0.0, min(1.0, (var - 1.0) / -0.4))", "SCALE_Z"),
                    P("abduction.l", "Action_abduction.l", "max(0.0, min(1.0, (var - 1.0) /  0.3))", "SCALE_Z"),
                ],
            },
            {
                "bones": ["c_index1", "c_middle1", "c_ring1", "c_pinky1"],
                "pairs": [
                    P("roll.l", "Action_roll.l", "max(0.0, min(1.0, var / -0.500))", "ROT_X", "QUATERNION"),
                    P("roll2.l", "Action_roll2.l", "max(0.0, min(1.0, var /  0.500))", "ROT_X", "QUATERNION"),
                    P("adduction.l", "Action_adduction.l", "max(0.0, min(1.0, (var - 1.0) / -0.4))", "SCALE_Z"),
                    P("abduction.l", "Action_abduction.l", "max(0.0, min(1.0, (var - 1.0) /  0.3))", "SCALE_Z"),
                ],
            },
            {
                "bones": ["c_index2", "c_index3", "c_middle2", "c_middle3",
                          "c_ring2", "c_ring3", "c_pinky2", "c_pinky3", "c_thumb3"],
                "pairs": [
                    P("claw.l", "Action_claw.l", "max(0.0, min(1.0, (var - 1.0) / -0.4))", "SCALE_X"),
                ],
            },
        ],
    },
    ".r": {
        "ctrl": "hand_control_R",
        "groups": [
            {
                "bones": ["c_pinky1_roll", "c_ring1_roll", "c_middle1_roll", "c_index1_roll", "c_thumb2_roll"],
                "pairs": [
                    P("fist.r", "Action_fist.r", "max(0.0, min(1.0, var /  0.03))", "LOC_X"),
                    P("extend.r", "Action_extend.r", "max(0.0, min(1.0, var / -0.03))", "LOC_X"),
                ],
            },
            {
                "bones": ["c_thumb1"],
                "pairs": [
                    P("fist.r", "Action_fist.r", "max(0.0, min(1.0, var /  0.03))", "LOC_X"),
                    P("extend.r", "Action_extend.r", "max(0.0, min(1.0, var / -0.03))", "LOC_X"),
                    P("roll.r", "Action_roll.r", "max(0.0, min(1.0, var /  0.500))", "ROT_X", "QUATERNION"),
                    P("roll2.r", "Action_roll2.r", "max(0.0, min(1.0, var / -0.500))", "ROT_X", "QUATERNION"),
                    P("adduction.r", "Action_adduction.r", "max(0.0, min(1.0, (var - 1.0) /  -0.4))", "SCALE_Z"),
                    P("abduction.r", "Action_abduction.r", "max(0.0, min(1.0, (var - 1.0) /   0.3))", "SCALE_Z"),
                ],
            },
            {
                "bones": ["c_index1", "c_middle1", "c_ring1", "c_pinky1"],
                "pairs": [
                    P("roll.r", "Action_roll.r", "max(0.0, min(1.0, var / -0.500))", "ROT_X", "QUATERNION"),
                    P("roll2.r", "Action_roll2.r", "max(0.0, min(1.0, var /  0.500))", "ROT_X", "QUATERNION"),
                    P("adduction.r", "Action_adduction.r", "max(0.0, min(1.0, (var - 1.0) /  -0.4))", "SCALE_Z"),
                    P("abduction.r", "Action_abduction.r", "max(0.0, min(1.0, (var - 1.0) /   0.3))", "SCALE_Z"),
                ],
            },
            {
                "bones": ["c_index2", "c_index3", "c_middle2", "c_middle3",
                          "c_ring2", "c_ring3", "c_pinky2", "c_pinky3", "c_thumb3"],
                "pairs": [
                    P("claw.r", "Action_claw.r", "max(0.0, min(1.0, (var - 1.0) / -0.4))", "SCALE_X"),
                ],
            },
        ],
    },
}


# ═══════════════════════════════════════════════════════════════════════════════

def safe_set(obj, attr, value):
    if hasattr(obj, attr):
        try:
            setattr(obj, attr, value)
        except Exception as e:
            print(f"  [warn] {attr} = {value!r} → {e}")
    else:
        print(f"  [warn] '{attr}' não existe nesta versão do Blender — pulado.")


def ensure_slot_name(action, display_name="rig"):
    if not hasattr(action, 'slots'):
        return
    if not action.slots:
        try:
            slot = action.slots.new("OBJECT", display_name)
        except Exception:
            pass
        return
    for slot in action.slots:
        safe_set(slot, 'name_display', display_name)


# ═══════════════════════════════════════════════════════════════════════════════

def split_side(name):
    for side in SIDES:
        if name.lower().endswith(side):
            return name[:-len(side)], name[-len(side):]
    return name, None


def get_finger_prefix(base):
    lower = base.lower()
    for prefix in FINGER_PREFIXES:
        if prefix in lower:
            return prefix
    return None


def is_roll_bone(name):
    return "_roll" in name.lower()


def is_finger_bone(name):
    if is_roll_bone(name):
        return False
    base, side = split_side(name)
    if side is None:
        return False
    if get_finger_prefix(base) is None:
        return False
    if any(excl in base.lower() for excl in EXCLUDE_SUBSTRINGS):
        return False
    return True


def is_thumb(name):
    return "thumb" in name.lower()


def get_roll_for_bone(name):
    _, side = split_side(name)
    base_roll = ROLL_THUMB if is_thumb(name) else ROLL_FINGERS
    return -base_roll if side == '.r' else base_roll


def make_roll_name(original):
    base, side = split_side(original)
    return (base + "_roll" + side) if side else (original + "_roll")


def segment_key(name):
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


def apply_offset(bone, name):
    if is_thumb(name):
        bone.head.y += Y_OFFSET
        bone.tail.y += Y_OFFSET
    else:
        bone.head.z += Z_OFFSET
        bone.tail.z += Z_OFFSET


# ═══════════════════════════════════════════════════════════════════════════════

def run_finger_controller(obj):
    arm = obj.data
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = arm.edit_bones

    finger_names = [b.name for b in edit_bones if is_finger_bone(b.name)]
    if not finger_names:
        bpy.ops.object.mode_set(mode='POSE')
        raise RuntimeError("No finger bones found. Check naming: c_thumb/c_index/c_middle/c_ring/c_pinky + .l/.r")

    groups = group_finger_bones(finger_names)

    print(f"\n[finger] Groups detected:")
    for (prefix, side), names in sorted(groups.items()):
        print(f"  ({prefix}, {side}): {names}")

    # ── Create _roll bones ────────────────────────────────────────────────────
    roll_map = {}
    created_order = []

    for (prefix, side), sorted_names in groups.items():
        for src_name in sorted_names:
            roll_name = make_roll_name(src_name)
            roll_map[src_name] = roll_name
            created_order.append((roll_name, src_name))

    for roll_name, src_name in created_order:
        if roll_name in edit_bones:
            print(f"  [skip] '{roll_name}' already exists.")
            continue
        src = edit_bones[src_name]
        new_bone = edit_bones.new(roll_name)
        new_bone.head = src.head.copy()
        new_bone.tail = src.tail.copy()
        new_bone.matrix = src.matrix.copy()
        new_bone.use_connect = False
        apply_offset(new_bone, roll_name)
        new_bone.roll = get_roll_for_bone(roll_name)

    # ── Parenting ─────────────────────────────────────────────────────────────
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

    for name in finger_names:
        if name in edit_bones:
            edit_bones[name].roll = get_roll_for_bone(name)

    bpy.ops.object.mode_set(mode='POSE')

    # ── Locks on _roll[0] ─────────────────────────────────────────────────────
    for (prefix, side), sorted_names in groups.items():
        first_roll = roll_map.get(sorted_names[0])
        if not first_roll:
            continue
        pb = obj.pose.bones.get(first_roll)
        if pb is None:
            continue
        pb.lock_location = (True, True, True)
        pb.lock_scale = (True, True, True)
        pb.lock_rotation = (False, True, True) if is_thumb(first_roll) else (True, True, False)

    # ── Copy Rotation: roll[i] → roll[i-1]  (Replace) ────────────────────────
    for (prefix, side), sorted_names in groups.items():
        roll_chain = [roll_map[n] for n in sorted_names if roll_map.get(n) in obj.pose.bones]
        for i in range(1, len(roll_chain)):
            src_pb = obj.pose.bones[roll_chain[i]]
            tgt_name = roll_chain[i - 1]
            for c in list(src_pb.constraints):
                if c.type == "COPY_ROTATION" and c.subtarget == tgt_name:
                    src_pb.constraints.remove(c)
            con = src_pb.constraints.new("COPY_ROTATION")
            con.target = obj
            con.subtarget = tgt_name
            con.mix_mode = "REPLACE"
            con.target_space = "LOCAL_OWNER_ORIENT"
            con.owner_space = "LOCAL"

    for (prefix, side), sorted_names in groups.items():
        for src_name in sorted_names:
            roll_name = roll_map.get(src_name)
            if not roll_name or src_name not in obj.pose.bones:
                continue
            pb = obj.pose.bones[src_name]
            for c in list(pb.constraints):
                if c.type == "COPY_ROTATION" and c.subtarget == roll_name:
                    pb.constraints.remove(c)
            con = pb.constraints.new("COPY_ROTATION")
            con.target = obj
            con.subtarget = roll_name
            con.mix_mode = "ADD"
            con.target_space = "LOCAL_OWNER_ORIENT"
            con.owner_space = "LOCAL"

    HIDDEN_COLL = "_roll_hidden"
    coll = arm.collections.get(HIDDEN_COLL) or arm.collections.new(HIDDEN_COLL)
    coll.is_visible = False
    for (prefix, side), sorted_names in groups.items():
        roll_chain = [roll_map[n] for n in sorted_names if roll_map.get(n)]
        for bone_name in roll_chain[1:]:
            bone = arm.bones.get(bone_name)
            if bone:
                coll.assign(bone)

    # ── Widgets ───────────────────────────────────────────────────────────────
    def assign_widget(pb, shape_name):
        bpy.ops.pose.select_all(action='DESELECT')
        pb.select = True
        obj.data.bones.active = pb.bone
        try:
            bpy.context.window_manager.widget_list = shape_name
            with bpy.context.temp_override(
                    active_object=obj, object=obj,
                    active_pose_bone=pb, selected_pose_bones=[pb],
            ):
                bpy.ops.bonewidget.create_widget()
            print(f"  [widget] '{pb.name}' ← {shape_name}")
        except Exception as e:
            print(f"  [widget] Error '{pb.name}': {e}")

    for (prefix, side), sorted_names in groups.items():
        roll_chain = [roll_map[n] for n in sorted_names if roll_map.get(n) in obj.pose.bones]
        if not roll_chain:
            continue
        assign_widget(obj.pose.bones[roll_chain[0]], "Sphere")
        if is_thumb(roll_chain[0]) and len(roll_chain) > 1:
            assign_widget(obj.pose.bones[roll_chain[0]], "Arrow Double (straight)")

    for (prefix, side), sorted_names in groups.items():
        roll_chain = [roll_map[n] for n in sorted_names if roll_map.get(n) in obj.pose.bones]
        for roll_name in roll_chain:
            obj.pose.bones[roll_name].color.palette = 'THEME01'

    print(f"\n[finger] Done.")
    return roll_map, groups


# ═══════════════════════════════════════════════════════════════════════════════

def load_actions_data(filepath):
    filepath = pathlib.Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"[actions] File not found: {filepath}")
    namespace = {}
    exec(filepath.read_text(encoding="utf-8"), namespace)
    if "ACTIONS_DATA" not in namespace:
        raise KeyError("[actions] ACTIONS_DATA not found in file.")
    return namespace["ACTIONS_DATA"]


def recreate_actions(actions_data, overwrite=OVERWRITE_EXISTING, fake_user=USE_FAKE_USER):
    created = []
    skipped = []

    for action_data in actions_data:
        name = action_data.get("name", "<no name>")

        if name in bpy.data.actions:
            if not overwrite:
                print(f"  [actions] Already exists, skipping: {name}")
                skipped.append(name)
                continue
            bpy.data.actions.remove(bpy.data.actions[name])

        action = bpy.data.actions.new(name)

        for fc_data in action_data.get("fcurves", []):
            try:
                fc = action.fcurves.new(
                    data_path=fc_data["data_path"],
                    index=fc_data["array_index"],
                    action_group=fc_data.get("group") or "",
                )
            except Exception as e:
                print(f"  [actions] F-Curve error '{fc_data['data_path']}': {e}")
                continue

            fc.extrapolation = fc_data.get("extrapolation", "CONSTANT")
            keyframes = fc_data.get("keyframes", [])
            if not keyframes:
                continue

            fc.keyframe_points.add(len(keyframes))
            fc.keyframe_points.foreach_set("co", [v for kp in keyframes for v in kp["co"]])
            fc.keyframe_points.foreach_set("handle_left", [v for kp in keyframes for v in kp["handle_left"]])
            fc.keyframe_points.foreach_set("handle_right", [v for kp in keyframes for v in kp["handle_right"]])
            for i, kp_data in enumerate(keyframes):
                kp = fc.keyframe_points[i]
                kp.handle_left_type = kp_data.get("handle_left_type", "AUTO")
                kp.handle_right_type = kp_data.get("handle_right_type", "AUTO")
                kp.interpolation = kp_data.get("interpolation", "BEZIER")
                kp.easing = kp_data.get("easing", "AUTO")
            fc.update()

        ensure_slot_name(action, "rig")

        action.use_fake_user = fake_user
        created.append(name)
        print(f"  [actions] Created: {name}  ({len(action.fcurves)} F-Curves)")

    print(f"\n[actions] Created: {len(created)}  Skipped: {len(skipped)}")
    return created


# ═══════════════════════════════════════════════════════════════════════════════

def make_action_constraint(pb, armature_obj, action, constr_name,
                           expr, transform_type, rotation_mode=None,
                           hand_control_bone=None):
    if constr_name in pb.constraints:
        pb.constraints.remove(pb.constraints[constr_name])

    con = pb.constraints.new('ACTION')
    con.name = constr_name
    con.target = armature_obj
    con.subtarget = ""
    con.action = action

    if hasattr(action, 'slots') and action.slots and hasattr(con, 'slot'):
        try:
            con.slot = action.slots[0]
        except Exception:
            pass

    safe_set(con, 'frame_start', 0)
    safe_set(con, 'frame_end', 10)
    con.influence = 1.0

    for mix_val in ('BEFORE_SPLIT', 'BEFORE'):
        try:
            con.mix_mode = mix_val
            break
        except (TypeError, AttributeError):
            continue
    safe_set(con, 'use_split_channels', True)

    channel_map = {
        'LOC_X': ('LOCATION_X', 'LOC_X'),
        'ROT_X': ('ROTATION_X', 'ROT_X'),
        'SCALE_X': ('SCALE_X',),
        'SCALE_Z': ('SCALE_Z',),
    }
    for channel_val in channel_map.get(transform_type, (transform_type,)):
        try:
            con.transform_channel = channel_val
            break
        except (TypeError, AttributeError):
            continue

    for space_val in ('LOCAL_OWNER_ORIENT', 'LOCAL_WITH_PARENT', 'LOCAL'):
        try:
            con.target_space = space_val
            break
        except (TypeError, AttributeError):
            continue

    for attr in ('range_min', 'min'): safe_set(con, attr, 0.0)
    for attr in ('range_max', 'max'): safe_set(con, attr, 1.0)

    for attr in ('use_evaluation_time', 'use_eval_time'):
        if hasattr(con, attr):
            try:
                setattr(con, attr, True)
                print(f"  [eval_time] '{attr}' = True ✓  ({pb.name} / {constr_name})")
                break
            except Exception as e:
                print(f"  [eval_time] '{attr}' erro: {e}")

    if expr and hand_control_bone:
        bone_name = pb.name
        driver_path = f'pose.bones["{bone_name}"].constraints["{constr_name}"].eval_time'
        try:
            armature_obj.driver_remove(driver_path)
        except Exception:
            pass
        try:
            fc_drv = armature_obj.driver_add(driver_path)
            drv = fc_drv.driver
            drv.type = 'SCRIPTED'
            drv.expression = expr
            for v in list(drv.variables):
                drv.variables.remove(v)
            v = drv.variables.new()
            v.name = 'var'
            v.type = 'TRANSFORMS'
            tgt = v.targets[0]
            tgt.id = armature_obj
            tgt.bone_target = hand_control_bone
            tgt.transform_type = transform_type
            tgt.transform_space = 'LOCAL_SPACE'
            if rotation_mode and hasattr(tgt, 'rotation_mode'):
                try:
                    tgt.rotation_mode = rotation_mode
                except Exception as e:
                    print(f"  [driver] rotation_mode error: {e}")
            print(f"  [driver] {bone_name} / {constr_name}  [{transform_type}]  →  {expr}")
        except Exception as e:
            print(f"  [driver] Error in '{constr_name}' ({bone_name}): {e}")

    return con


def add_action_constraints(armature_obj):
    pose_bones = armature_obj.pose.bones
    for side, side_data in ACTION_CONSTRAINT_MAP.items():
        ctrl_bone = side_data["ctrl"]
        for group in side_data["groups"]:
            for bone_base in group["bones"]:
                full_name = bone_base + side
                pb = pose_bones.get(full_name)
                if pb is None:
                    print(f"  [constraints] Bone '{full_name}' not found — skipped.")
                    continue
                for pair in group["pairs"]:
                    action = bpy.data.actions.get(pair["action"])
                    if action is None:
                        print(f"  [constraints] Action '{pair['action']}' not found — skipping {full_name}.")
                        continue
                    make_action_constraint(
                        pb=pb,
                        armature_obj=armature_obj,
                        action=action,
                        constr_name=pair["constraint"],
                        expr=pair["expr"],
                        transform_type=pair["type"],
                        rotation_mode=pair.get("rot_mode"),
                        hand_control_bone=ctrl_bone,
                    )
                    print(f"  [constraints] {full_name}  ←  {pair['constraint']}")


# ═══════════════════════════════════════════════════════════════════════════════

def run_hand_controller(obj):
    arm = obj.data

    # ── hand_control_L / _R ─────────────────────────────
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = arm.edit_bones
    created_bones = []

    for bone_suffix, parent_suffix, x_sign in BONE_CONFIGS:
        bone_name = BONE_BASE_NAME + bone_suffix
        parent_name = "hand" + parent_suffix

        if bone_name in edit_bones:
            edit_bones.remove(edit_bones[bone_name])

        eb = edit_bones.new(bone_name)

        ik_bone_name = "c_hand_ik" + parent_suffix
        ik_bone = edit_bones.get(ik_bone_name)
        if ik_bone is not None:
            mid = (ik_bone.head + ik_bone.tail) / 2.0
            ctrl_x = mid.x
            ctrl_y = mid.y
            ctrl_z = mid.z + HAND_CONTROL_Z_OFFSET
            print(f"  [hand] '{bone_name}' a partir do centro de '{ik_bone_name}' "
                  f"mid=({mid.x:.4f}, {mid.y:.4f}, {mid.z:.4f}) "
                  f"-> ({ctrl_x:.4f}, {ctrl_y:.4f}, {ctrl_z:.4f})")
        else:
            hand_bone = edit_bones.get(parent_name)
            if hand_bone:
                mid = (hand_bone.head + hand_bone.tail) / 2.0
                ctrl_x = mid.x
                ctrl_y = mid.y
                ctrl_z = mid.z + HAND_CONTROL_Z_OFFSET
            else:
                ctrl_x = ctrl_y = ctrl_z = 0.0
            print(f"  [hand] '{ik_bone_name}' nao encontrado -- fallback via '{parent_name}'.")

        eb.head = (ctrl_x, ctrl_y, ctrl_z)
        eb.tail = (ctrl_x, ctrl_y, ctrl_z + HAND_CONTROL_LEN)
        eb.use_connect = False

        if parent_name in edit_bones:
            eb.parent = edit_bones[parent_name]
            print(f"  [hand] {bone_name} → parent: {parent_name}")
        else:
            print(f"  [hand] Parent '{parent_name}' not found.")

        created_bones.append(bone_name)

    # ── locks + widget + limit constraints ──────────────────────────
    bpy.ops.object.mode_set(mode='POSE')

    for bone_name in created_bones:
        pb = obj.pose.bones.get(bone_name)
        if pb is None:
            continue

        pb.lock_location = (False, True, True)
        pb.lock_scale = (False, True, False)
        pb.lock_rotation = (False, True, True)
        pb.color.palette = 'THEME12'

        try:
            bpy.ops.pose.select_all(action='DESELECT')
            pb.select = True
            obj.data.bones.active = pb.bone
            bpy.context.window_manager.widget_list = WIDGET_SHAPE
            with bpy.context.temp_override(
                    active_object=obj, object=obj,
                    active_pose_bone=pb, selected_pose_bones=[pb],
            ):
                bpy.ops.bonewidget.create_widget(
                    relative_size=True, global_size_simple=1.00,
                    slide_simple=0.00,
                    rotation=(WIDGET_ROT_X, WIDGET_ROT_Y, WIDGET_ROT_Z),
                    wireframe_width=WIDGET_WIRE_WIDTH,
                )
            print(f"  [hand] Widget '{WIDGET_SHAPE}' → {bone_name}")
        except Exception as e:
            print(f"  [hand] Widget error {bone_name}: {e}")

        for c in list(pb.constraints):
            if c.type in ("LIMIT_LOCATION", "LIMIT_ROTATION", "LIMIT_SCALE"):
                pb.constraints.remove(c)

        ll = pb.constraints.new("LIMIT_LOCATION")
        ll.use_min_x = True;
        ll.min_x = -0.03
        ll.use_min_y = True;
        ll.min_y = -0.05
        ll.use_min_z = False
        ll.use_max_x = True;
        ll.max_x = 0.03
        ll.use_max_y = True;
        ll.max_y = 0.05
        ll.use_max_z = False
        ll.use_transform_limit = True
        ll.owner_space = 'LOCAL';
        ll.influence = 1.0

        lr = pb.constraints.new("LIMIT_ROTATION")
        lr.use_limit_x = True
        lr.min_x = math.radians(-35);
        lr.max_x = math.radians(35)
        lr.use_limit_y = False;
        lr.use_limit_z = False
        lr.euler_order = 'AUTO'
        lr.use_transform_limit = True
        lr.owner_space = 'LOCAL';
        lr.influence = 1.0
        safe_set(lr, 'use_legacy_behavior', True)

        ls = pb.constraints.new("LIMIT_SCALE")
        ls.use_min_x = True;
        ls.min_x = 0.6
        ls.use_min_y = False
        ls.use_min_z = True;
        ls.min_z = 0.6
        ls.use_max_x = True;
        ls.max_x = 1.0
        ls.use_max_y = False
        ls.use_max_z = True;
        ls.max_z = 1.3
        ls.use_transform_limit = True
        ls.owner_space = 'LOCAL';
        ls.influence = 1.0

        print(f"  [hand] Limit constraints → {bone_name}")

    # ── Actions,  Action Constraints and drivers ───────────────────────────────────────────────────────────────

    try:
        actions_data = load_actions_data(ACTIONS_PATH)
    except Exception as e:
        print(f"  [hand] Error loading actions data: {e}")

    recreate_actions(actions_data)
    add_action_constraints(obj)

    print(f"\n[hand] Done. Bones: {created_bones}")


# ═══════════════════════════════════════════════════════════════════════════════

def run():
    obj = bpy.context.active_object
    if obj is None or obj.type != 'ARMATURE':
        raise RuntimeError("Select an Armature before running the script.")

    print("\n" + "═" * 60)
    print("  STEP 1 — FINGER CONTROLLER")
    print("═" * 60)
    run_finger_controller(obj)

    print("\n" + "═" * 60)
    print("  STEP 2 — HAND CONTROLLER")
    print("═" * 60)
    run_hand_controller(obj)

    print("\n" + "═" * 60)
    print("  ALL DONE")
    print("═" * 60)


run()