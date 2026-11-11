# ═══════════════════════════════════════════════════════════════════════════════
#  UMA RIG TOOLS — Blender Addon
#  Combines: Eye Rig, Finger Controller, Hand Controller, Ear Roll,
#            Shape Keys Combiner, Skeleton Cleanup
# ═══════════════════════════════════════════════════════════════════════════════

bl_info = {
    "name":        "Uma Rig Tools",
    "author":      "ryujin",
    "version":     (1, 0, 11),
    "blender":     (5, 0, 0),
    "location":    "View3D > N-Panel > Uma Rig",
    "description": "Complete UmaMusume rig automation: eyes, fingers, hands, ears, shape keys",
    "category":    "Rigging",
}

import bpy
import math
import mathutils
import re
import pathlib
from collections import defaultdict
from bpy.types  import Panel, Operator, PropertyGroup, UIList
from bpy.props  import (StringProperty, FloatProperty, BoolProperty,
                         PointerProperty, CollectionProperty, IntProperty,
                         FloatVectorProperty)


# ─────────────────────────────────────────────────────────────────────────────
#  UTILS
# ─────────────────────────────────────────────────────────────────────────────

def _addon_dir() -> pathlib.Path:
    return pathlib.Path(__file__).parent


def _actions_path() -> pathlib.Path:
    return _addon_dir() / "actions.py"


def _poll_armature(self, obj):
    return obj.type == 'ARMATURE'

def _poll_mesh(self, obj):
    return obj.type == 'MESH'


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


# ─────────────────────────────────────────────────────────────────────────────
#  FINGER + HAND CONTROLLER LOGIC
# ─────────────────────────────────────────────────────────────────────────────

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

OVERWRITE_EXISTING = False
USE_FAKE_USER = True


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


FINGERTIP_MIN_WEIGHT     = 0.4
FINGERTIP_AXIS_TOLERANCE = 0.5


def _find_vertex_group_ci(mesh_obj, bone_name):
    vg = mesh_obj.vertex_groups.get(bone_name)
    if vg is not None:
        return vg
    bone_name_l = bone_name.lower()
    for vg in mesh_obj.vertex_groups:
        if vg.name.lower() == bone_name_l:
            return vg
    return None


def _find_tip_vertex_world(mesh_obj, bone_name, anchor_world, direction, axis_tolerance):
    vg = _find_vertex_group_ci(mesh_obj, bone_name)
    if vg is None:
        return None
    vg_index = vg.index
    mesh_mat = mesh_obj.matrix_world

    candidates = []
    for v in mesh_obj.data.vertices:
        weight = next((g.weight for g in v.groups if g.group == vg_index), 0.0)
        if weight < FINGERTIP_MIN_WEIGHT:
            continue
        world_co = mesh_mat @ v.co
        offset = world_co - anchor_world
        d = offset.dot(direction)
        if d <= 0:
            continue
        perp = (offset - direction * d).length
        candidates.append((d, perp, world_co))

    if not candidates:
        return None

    on_axis = [c for c in candidates if c[1] <= axis_tolerance]
    pool = on_axis if on_axis else candidates
    best = max(pool, key=lambda c: c[0])
    return best[2]


def snap_fingertips_to_mesh(edit_bones, groups, mesh_obj, arm_obj):
    arm_mat = arm_obj.matrix_world
    arm_mat_inv = arm_mat.inverted()
    fixed, skipped = [], []
    for (prefix, side), sorted_names in groups.items():
        if not sorted_names:
            continue
        tip_name = sorted_names[-1]
        tip_bone = edit_bones.get(tip_name)
        if tip_bone is None:
            skipped.append(tip_name); continue

        ref_bone = edit_bones.get(sorted_names[-2]) if len(sorted_names) >= 2 else None
        if ref_bone is None:
            ref_bone = tip_bone

        ref_head_world = arm_mat @ ref_bone.head
        ref_tail_world = arm_mat @ ref_bone.tail
        direction_raw = ref_tail_world - ref_head_world
        if direction_raw.length < 1e-8:
            skipped.append(tip_name); continue
        ref_length = direction_raw.length
        direction = direction_raw.normalized()
        axis_tolerance = ref_length * FINGERTIP_AXIS_TOLERANCE

        tip_head_world = arm_mat @ tip_bone.head
        tip_world = _find_tip_vertex_world(mesh_obj, tip_name, tip_head_world, direction, axis_tolerance)
        if tip_world is None:
            skipped.append(tip_name); continue
        tip_bone.tail = arm_mat_inv @ tip_world
        fixed.append(tip_name)
    return fixed, skipped


# ═══════════════════════════════════════════════════════════════════════════════

def run_finger_controller(obj, mesh_obj=None):
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

    if mesh_obj is not None:
        fixed, skipped = snap_fingertips_to_mesh(edit_bones, groups, mesh_obj, obj)
        print(f"[finger] Fingertips snapped to mesh: {fixed}")
        if skipped:
            print(f"[finger] Fingertips skipped (no matching vertex group / weights): {skipped}")
    else:
        print("[finger] No Body Mesh set — skipping fingertip snap.")

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

    try:
        actions_data = load_actions_data(_actions_path())
    except Exception as e:
        print(f"  [hand] Error loading actions data: {e}")
        actions_data = []

    recreate_actions(actions_data)
    add_action_constraints(obj)

    print(f"\n[hand] Done. Bones: {created_bones}")

# ─────────────────────────────────────────────────────────────────────────────
#  EAR ROLL LOGIC
# ─────────────────────────────────────────────────────────────────────────────

EAR_PREFIX = "Ear_"
EAR_SIDES  = ["_L", "_R"]

def _split_ear_side(name):
    for side in EAR_SIDES:
        if name.endswith(side):
            return name[:-len(side)], side
    return name, None

def _is_ear_bone(name):
    if "_roll" in name.lower(): return False
    base, side = _split_ear_side(name)
    return side is not None and base.startswith(EAR_PREFIX)

def _make_ear_roll_name(original):
    base, side = _split_ear_side(original)
    return (base + "_roll" + side) if side else (original + "_roll")

def _ear_segment_key(name):
    base, _ = _split_ear_side(name)
    nums = re.findall(r'\d+', base)
    return int(nums[-1]) if nums else 0


def run_ear_controller(obj):
    arm = obj.data
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = arm.edit_bones

    ear_names = [b.name for b in edit_bones if _is_ear_bone(b.name)]
    if not ear_names:
        bpy.ops.object.mode_set(mode='POSE')
        raise RuntimeError("No ear bones found (Ear_NN_L / Ear_NN_R).")

    groups = {side: [] for side in EAR_SIDES}
    for name in ear_names:
        _, side = _split_ear_side(name)
        if side: groups[side].append(name)
    for side in groups:
        groups[side].sort(key=_ear_segment_key)

    roll_map = {}
    for side, sorted_names in groups.items():
        for src_name in sorted_names:
            rn = _make_ear_roll_name(src_name)
            roll_map[src_name] = rn
            if rn in edit_bones: continue
            src = edit_bones[src_name]
            nb = edit_bones.new(rn)
            nb.head=src.head.copy(); nb.tail=src.tail.copy()
            nb.matrix=src.matrix.copy(); nb.roll=src.roll; nb.use_connect=False

    for side, sorted_names in groups.items():
        for i, src_name in enumerate(sorted_names):
            rn = roll_map[src_name]
            if rn not in edit_bones: continue
            rb = edit_bones[rn]
            if i == 0:
                if "head.x" in edit_bones:
                    rb.parent = edit_bones["head.x"]
            else:
                prev = roll_map[sorted_names[i-1]]
                if prev in edit_bones: rb.parent = edit_bones[prev]
            rb.use_connect = False

    bpy.ops.object.mode_set(mode='POSE')

    for side, sorted_names in groups.items():
        chain = [roll_map[n] for n in sorted_names if roll_map.get(n) in obj.pose.bones]
        for i in range(1, len(chain)):
            pb = obj.pose.bones[chain[i]]; tgt = chain[i-1]
            for c in list(pb.constraints):
                if c.type=="COPY_ROTATION" and c.subtarget==tgt: pb.constraints.remove(c)
            con = pb.constraints.new("COPY_ROTATION")
            con.target=obj; con.subtarget=tgt; con.mix_mode="REPLACE"
            con.target_space="LOCAL_OWNER_ORIENT"; con.owner_space="LOCAL"

    for side, sorted_names in groups.items():
        for src_name in sorted_names:
            rn = roll_map.get(src_name)
            if not rn or src_name not in obj.pose.bones: continue
            pb = obj.pose.bones[src_name]
            for c in list(pb.constraints):
                if c.type=="COPY_ROTATION" and c.subtarget==rn: pb.constraints.remove(c)
            con = pb.constraints.new("COPY_ROTATION")
            con.target=obj; con.subtarget=rn; con.mix_mode="ADD"
            con.target_space="LOCAL_OWNER_ORIENT"; con.owner_space="LOCAL"

    for side, sorted_names in groups.items():
        rz = roll_map.get(sorted_names[0])
        if not rz or rz not in obj.pose.bones: continue
        pb = obj.pose.bones[rz]
        bpy.ops.pose.select_all(action='DESELECT')
        pb.select=True; obj.data.bones.active=pb.bone
        mirror = -1 if side=="_R" else 1
        try:
            bpy.context.window_manager.widget_list="Roll 1"
            with bpy.context.temp_override(active_object=obj,object=obj,
                    active_pose_bone=pb,selected_pose_bones=[pb]):
                bpy.ops.bonewidget.create_widget(relative_size=True,
                    global_size_simple=1.00,slide_simple=0.00,
                    rotation=(math.radians(-9*mirror),math.radians(0),math.radians(-18*mirror)),
                    wireframe_width=2.00)
        except Exception as e:
            print(f"  [ear] Widget error: {e}")

    HIDDEN_COLL="_roll_hidden"
    coll = arm.collections.get(HIDDEN_COLL) or arm.collections.new(HIDDEN_COLL)
    coll.is_visible=False
    for side, sorted_names in groups.items():
        chain=[roll_map[n] for n in sorted_names if roll_map.get(n)]
        for bn in chain[1:]:
            bone=arm.bones.get(bn)
            if bone: coll.assign(bone)

    print("[ear] Done.")


# ─────────────────────────────────────────────────────────────────────────────
#  CLEANUP LOGIC
# ─────────────────────────────────────────────────────────────────────────────

HAND_CONTROL_BONES = ["hand_control_L", "hand_control_R"]

HIDDEN_COLL_NAME = "_roll_hidden"

ACTION_NAMES = [
    "fist.l", "fist.r",
    "extend.l", "extend.r",
    "roll.l", "roll.r",
    "roll2.l", "roll2.r",
    "adduction.l", "adduction.r",
    "abduction.l", "abduction.r",
    "claw.l", "claw.r",
]

ACTION_CONSTRAINT_NAMES = [
    "Action_fist.l", "Action_fist.r",
    "Action_extend.l", "Action_extend.r",
    "Action_roll.l", "Action_roll.r",
    "Action_roll2.l", "Action_roll2.r",
    "Action_adduction.l", "Action_adduction.r",
    "Action_abduction.l", "Action_abduction.r",
    "Action_claw.l", "Action_claw.r",
]

HAND_CTRL_CONSTRAINT_TYPES = ("LIMIT_LOCATION", "LIMIT_ROTATION", "LIMIT_SCALE")

FINGER_CONSTRAINT_TYPES = ("COPY_ROTATION",)


def is_finger_bone_base(name):
    prefixes = ["c_thumb", "c_index", "c_middle", "c_ring", "c_pinky"]
    sides = [".l", ".r"]
    lower = name.lower()
    return (any(lower.startswith(p) for p in prefixes)
            and any(lower.endswith(s) for s in sides))


def run_cleanup(obj):
    arm = obj.data

    bpy.ops.object.mode_set(mode='POSE')
    removed_constraints = 0
    removed_drivers = 0

    for pb in obj.pose.bones:
        for c in list(pb.constraints):
            if c.name in ACTION_CONSTRAINT_NAMES:
                driver_path = f'pose.bones["{pb.name}"].constraints["{c.name}"].eval_time'
                try:
                    obj.driver_remove(driver_path)
                    removed_drivers += 1
                except Exception:
                    pass
                pb.constraints.remove(c)
                removed_constraints += 1

        if is_finger_bone_base(pb.name) or is_roll_bone(pb.name):
            for c in list(pb.constraints):
                if c.type == "COPY_ROTATION":
                    pb.constraints.remove(c)
                    removed_constraints += 1

        if pb.name.startswith("Ear_"):
            for c in list(pb.constraints):
                if c.type == "COPY_ROTATION":
                    pb.constraints.remove(c)
                    removed_constraints += 1

        if pb.name in HAND_CONTROL_BONES:
            for c in list(pb.constraints):
                if c.type in HAND_CTRL_CONSTRAINT_TYPES:
                    pb.constraints.remove(c)
                    removed_constraints += 1

    print(f"  [cleanup] Constraints removidas : {removed_constraints}")
    print(f"  [cleanup] Drivers removidos      : {removed_drivers}")

    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = arm.edit_bones
    removed_bones = 0

    bones_to_remove = (
            [b.name for b in edit_bones if is_roll_bone(b.name)]
            + [b for b in HAND_CONTROL_BONES if b in edit_bones]
    )

    for bone_name in bones_to_remove:
        if bone_name in edit_bones:
            edit_bones.remove(edit_bones[bone_name])
            removed_bones += 1
            print(f"  [cleanup] Bone removido: {bone_name}")

    print(f"  [cleanup] Total bones removidos: {removed_bones}")

    coll = arm.collections.get(HIDDEN_COLL_NAME)
    if coll:
        arm.collections.remove(coll)
        print(f"  [cleanup] Bone Collection '{HIDDEN_COLL_NAME}' removida.")

    bpy.ops.object.mode_set(mode='POSE')
    removed_actions = 0

    for action_name in ACTION_NAMES:
        action = bpy.data.actions.get(action_name)
        if action is None:
            continue
        action.use_fake_user = False
        if action.users == 0:
            bpy.data.actions.remove(action)
            removed_actions += 1
            print(f"  [cleanup] Action removida: {action_name}")
        else:
            print(f"  [cleanup] Action '{action_name}' ainda em uso ({action.users} users) — mantida.")

    print(f"  [cleanup] Actions removidas: {removed_actions}")

    bpy.ops.object.mode_set(mode='POSE')

    print("\n[cleanup] Done!")


# ─────────────────────────────────────────────────────────────────────────────
#  SKELETON CLEANUP
# ─────────────────────────────────────────────────────────────────────────────

def run_skeleton_cleanup(obj):
    arm = obj.data
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = arm.edit_bones

    to_remove = []
    for b in edit_bones:
        n = b.name
        if n.lower().endswith("handle") or re.match(r'^Sp_He_Ear0_', n):
            to_remove.append(n)

    removed = 0
    for bn in to_remove:
        if bn in edit_bones:
            edit_bones.remove(edit_bones[bn])
            removed += 1
            print(f"  [skel_cleanup] Removed: {bn}")

    bpy.ops.object.mode_set(mode='POSE')
    print(f"  [skel_cleanup] {removed} bones removed.")
    return removed


# ─────────────────────────────────────────────────────────────────────────────
#  SHAPE KEYS COMBINER LOGIC
# ─────────────────────────────────────────────────────────────────────────────

SEPARATOR_NAME = "==== both ===="

def run_shape_keys_combiner(obj):
    if not obj or not obj.data.shape_keys:
        raise RuntimeError("No object with shape keys found.")

    shape_keys = obj.data.shape_keys.key_blocks
    pairs = {}

    for sk in shape_keys:
        name = sk.name
        if 'xrange' in name.lower() or 'yrange' in name.lower(): continue
        if '_R(' in name or '_R[' in name or name.endswith('_R'):
            base = (name.replace('_R','',1) if name.endswith('_R')
                    else name.replace('_R(','(').replace('_R[','['))
            pairs.setdefault(base,{})['R'] = sk
        elif '_L(' in name or '_L[' in name or name.endswith('_L'):
            base = (name.replace('_L','',1) if name.endswith('_L')
                    else name.replace('_L(','(').replace('_L[','['))
            pairs.setdefault(base,{})['L'] = sk

    valid_pairs = {k:v for k,v in pairs.items() if 'L' in v and 'R' in v}
    if not valid_pairs:
        raise RuntimeError("No _L/_R pairs found.")

    if SEPARATOR_NAME not in shape_keys:
        sep = obj.shape_key_add(name=SEPARATOR_NAME, from_mix=False)
        sep.value=0.0; sep.mute=True; sep.lock_shape=True
        sep.slider_min=0.0; sep.slider_max=0.0

    created = 0
    for base_name, pair in valid_pairs.items():
        if base_name in shape_keys: continue
        obj.shape_key_add(name=base_name, from_mix=False)
        new_sk = shape_keys[base_name]; new_sk.value=0.0
        sk_l=pair['L']; sk_r=pair['R']; basis=shape_keys[0]
        for i,_ in enumerate(obj.data.vertices):
            dl = sk_l.data[i].co - basis.data[i].co
            dr = sk_r.data[i].co - basis.data[i].co
            new_sk.data[i].co = basis.data[i].co + dl + dr
        created+=1
        print(f"  [shape_keys] Created: {base_name}")
    print(f"[shape_keys] {created} key(s) created.")
    return created


# ─────────────────────────────────────────────────────────────────────────────
#  EYE RIG LOGIC
# ─────────────────────────────────────────────────────────────────────────────

EYE_LOCATOR_L        = "Eye_locator_L"
EYE_LOCATOR_R        = "Eye_locator_R"
EYE_CONTROL_BONE     = "eye_control"
SK_XRANGE_L          = "Eye_20_L(XRange)[M_Face]"
SK_XRANGE_R          = "Eye_20_R(XRange)[M_Face]"
SK_YRANGE_L          = "Eye_21_L(YRange)[M_Face]"
SK_YRANGE_R          = "Eye_21_R(YRange)[M_Face]"
SK_CLOSE_L           = "Eye_2_L(CloseA)[M_Face]"
SK_CLOSE_R           = "Eye_2_R(CloseA)[M_Face]"
SK_ODOROKI_L         = "Eye_12_L(OdorokiA)[M_Face]"
SK_ODOROKI_R         = "Eye_12_R(OdorokiA)[M_Face]"
ALLOWED_EXPR_CHARS   = re.compile(r'^[0-9a-zA-Z_\+\-\*/\(\)\.\,\s<>=!&|%^~]+$')
DANGEROUS_KEYWORDS   = ("import","exec","eval","open","os","__","globals",
                         "locals","getattr","setattr","delattr","compile",
                         "input","print","exit","quit","breakpoint")

EYE_DRIVER_DEFS = (
    {"label":"Eye_20_L  XRange",  "icon":'EVENT_L', "kind":'expr',
     "min":"xrange_l_min", "max":"xrange_l_max", "expr":"xrange_l_expr"},
    {"label":"Eye_20_R  XRange",  "icon":'EVENT_R', "kind":'expr',
     "min":"xrange_r_min", "max":"xrange_r_max", "expr":"xrange_r_expr"},
    {"label":"Eye_21_L  YRange",  "icon":'EVENT_L', "kind":'expr',
     "min":"yrange_l_min", "max":"yrange_l_max", "expr":"yrange_l_expr"},
    {"label":"Eye_21_R  YRange",  "icon":'EVENT_R', "kind":'expr',
     "min":"yrange_r_min", "max":"yrange_r_max", "expr":"yrange_r_expr"},
    {"label":"Eye_2_L  Close",    "icon":'EVENT_L', "kind":'close',
     "min":"close_l_min",   "max":"close_l_max",   "min_label":"Closed",  "max_label":"Open"},
    {"label":"Eye_2_R  Close",    "icon":'EVENT_R', "kind":'close',
     "min":"close_r_min",   "max":"close_r_max",   "min_label":"Closed",  "max_label":"Open"},
    {"label":"Eye_12_L  Odoroki", "icon":'EVENT_L', "kind":'odoroki',
     "min":"odoroki_l_min", "max":"odoroki_l_max", "min_label":"Neutral", "max_label":"Wide"},
    {"label":"Eye_12_R  Odoroki", "icon":'EVENT_R', "kind":'odoroki',
     "min":"odoroki_r_min", "max":"odoroki_r_max", "min_label":"Neutral", "max_label":"Wide"},
)

def _safe_denom(d):
    if abs(d) < 1e-6: return 1e-6 if d >= 0 else -1e-6
    return d

def _build_close_expr(closed, open_):
    return f"min(max(({open_}-var)/({_safe_denom(open_-closed)}),0.0),1.0)"

def _build_odoroki_expr(neutral, wide):
    return f"min(max((var-{neutral})/({_safe_denom(wide-neutral)}),0.0),1.0)"

def validate_expression(expr):
    expr=expr.strip()
    if not expr: return False,"Expression cannot be empty."
    if len(expr)>256: return False,"Expression too long."
    low=expr.lower()
    for kw in DANGEROUS_KEYWORDS:
        if kw in low: return False,f"Forbidden keyword: '{kw}'"
    if not ALLOWED_EXPR_CHARS.match(expr): return False,"Invalid characters."
    if "var" not in expr: return False,"Expression must reference 'var'."
    try:
        compile(expr,"<expr>","eval")
        result=eval(compile(expr,"<expr>","eval"),{"__builtins__":{}},
                    {"var":0.5,"min":min,"max":max,"abs":abs,"round":round})
        if not isinstance(result,(int,float)): return False,"Must evaluate to a number."
    except SyntaxError as e: return False,f"Syntax error: {e.msg}"
    except Exception as ex:  return False,f"Runtime error: {ex}"
    return True,""


BONE_DEFS = {
    "eye_control": {
        "parent": "c_head.x",
        "head": (0.0, -0.06990966945886612, 1.4768413305282593),
        "tail": (0.0, -0.06990966945886612, 1.5368413925170898),
        "matrix_local": (
            (1.0, 0.0, -8.470329472543003e-22, 0.0),
            (-8.470329472543003e-22, 0.0, -1.0, -0.06990966945886612),
            (0.0, 0.9999999403953552, 0.0, 1.4768413305282593),
            (0.0, 0.0, 0.0, 1.0),
        ),
        "use_deform": True,
        "collections": ["Main"],
        "custom_props": {"bonex_enable": False},
        "copy_location_target": None,
    },
    "Eye_locator_R": {
        "parent": "head.x",
        "head": (-0.04172586649656296, -0.03387831896543503, 1.4763139486312866),
        "tail": (-0.04172583669424057, -0.05630812048912048, 1.4763880968093872),
        "matrix_local": (
            (0.9999999403953552, 1.3286858120409306e-06, -0.000402359408326447, -0.04172586649656296),
            (-1.4291678951394715e-09, -0.9999945759773254, -0.003305733436718583, -0.03387831896543503),
            (-0.0004023615620099008, 0.0033057706896215677, -0.9999945163726807, 1.4763139486312866),
            (0.0, 0.0, 0.0, 1.0),
        ),
        "use_deform": True,
        "collections": ["Main"],
        "custom_props": {"cc": 1, "bonex_enable": False},
        "copy_location_target": "eye_control",
    },
    "Eye_locator_L": {
        "parent": "head.x",
        "head": (0.04172586649656296, -0.03387831896543503, 1.4763139486312866),
        "tail": (0.04172583669424057, -0.05630812048912048, 1.4763880968093872),
        "matrix_local": (
            (0.9999999403953552, -1.3286858120409306e-06, 0.000402359408326447, 0.04172586649656296),
            (1.4291465788573987e-09, -0.9999945759773254, -0.003305733436718583, -0.03387831896543503),
            (0.0004023615620099008, 0.0033057706896215677, -0.9999945163726807, 1.4763139486312866),
            (0.0, 0.0, 0.0, 1.0),
        ),
        "use_deform": True,
        "collections": ["Main"],
        "custom_props": {"cc": 1, "bonex_enable": False},
        "copy_location_target": "eye_control",
    },
}

BBONE_X = 0.10000000149011612
BBONE_Z = 0.10000000149011612
ENVELOPE_DISTANCE_CONTROL = 0.25
ENVELOPE_DISTANCE_LOCATOR = 0.07009346038103104


def build_eye_rig_controller(context, arm_obj, props):
    view_layer = context.view_layer
    prev_active = view_layer.objects.active
    prev_mode = prev_active.mode if prev_active else 'OBJECT'

    # Clean up old widget objects
    old_widgets = ["WGT-rig_eye_control", "WGT-rig_Eye_locator_R", "WGT-rig_Eye_locator_L"]
    for name in old_widgets:
        obj = bpy.data.objects.get(name)
        if obj:
            bpy.data.objects.remove(obj, do_unlink=True)

    view_layer.objects.active = arm_obj
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = arm_obj.data.edit_bones

    for bname in BONE_DEFS:
        if bname in edit_bones:
            edit_bones.remove(edit_bones[bname])

    for bname, d in BONE_DEFS.items():
        eb = edit_bones.new(bname)
        eb.head = mathutils.Vector(d["head"])
        eb.tail = mathutils.Vector(d["tail"])
        mat = mathutils.Matrix(d["matrix_local"])
        eb.align_roll(mat.col[2].xyz)
        eb.use_deform = d["use_deform"]
        eb.bbone_x = BBONE_X
        eb.bbone_z = BBONE_Z
        eb.envelope_distance = (
            ENVELOPE_DISTANCE_CONTROL if bname == "eye_control" else ENVELOPE_DISTANCE_LOCATOR
        )
        parent_name = d["parent"]
        if parent_name in edit_bones:
            eb.parent = edit_bones[parent_name]
        else:
            print(f"[eye rig] Aviso: parent '{parent_name}' não encontrado para '{bname}'.")

    bpy.ops.object.mode_set(mode='POSE')

    for bname, d in BONE_DEFS.items():
        pb = arm_obj.pose.bones[bname]

        for k, v in d["custom_props"].items():
            pb[k] = v

        bone = pb.bone
        bone.collections.clear()
        for cname in d["collections"]:
            coll = arm_obj.data.collections.get(cname)
            if coll is None:
                coll = arm_obj.data.collections.new(cname)
            coll.assign(bone)

        # Remove all existing constraints (we'll only add Copy Location)
        for c in list(pb.constraints):
            pb.constraints.remove(c)

        # Only Copy Location constraint for locators (no limits)
        if d["copy_location_target"]:
            copy_loc = pb.constraints.new('COPY_LOCATION')
            copy_loc.name = "Copy Location"
            copy_loc.target = arm_obj
            copy_loc.subtarget = d["copy_location_target"]
            copy_loc.head_tail = 0.0
            copy_loc.target_space = 'LOCAL_OWNER_ORIENT'
            copy_loc.owner_space = 'LOCAL'
            copy_loc.use_offset = True

    # ── Assign Bone Widget shapes and colors ──────────────────────────────
    for bname in BONE_DEFS:
        pb = arm_obj.pose.bones[bname]
        bpy.ops.pose.select_all(action='DESELECT')
        pb.select = True
        arm_obj.data.bones.active = pb.bone

        if bname == "eye_control":
            widget_name = "Eye Target 2"
            rotation = (math.radians(90), 0, 0)
            color_palette = "THEME03"
        else:
            widget_name = "Circle"
            rotation = (0, 0, 0)
            color_palette = "THEME01"

        try:
            bpy.context.window_manager.widget_list = widget_name
            with bpy.context.temp_override(
                    active_object=arm_obj, object=arm_obj,
                    active_pose_bone=pb, selected_pose_bones=[pb],
            ):
                bpy.ops.bonewidget.create_widget(
                    relative_size=True,
                    global_size_simple=1.00,
                    slide_simple=0.00,
                    rotation=rotation,
                    wireframe_width=2.00,
                )
            pb.color.palette = color_palette

            if bname == "eye_control":
                pb.custom_shape_scale_xyz = (1.2, 1.2, 1.2)

            print(f"  [eye rig] Widget '{widget_name}' + cor {color_palette} → {bname}")
        except Exception as e:
            print(f"  [eye rig] Erro ao criar widget para {bname}: {e}")

    bpy.ops.object.mode_set(mode=prev_mode if prev_mode in ('OBJECT', 'POSE') else 'OBJECT')
    if prev_active is not None:
        view_layer.objects.active = prev_active

    return {b: arm_obj.pose.bones[b] for b in BONE_DEFS}


def _remove_driver(shape_keys,sk_name):
    if not shape_keys.animation_data: return
    fc=shape_keys.animation_data.drivers.find(f'key_blocks["{sk_name}"].value')
    if fc: shape_keys.animation_data.drivers.remove(fc)

def _setup_location_driver(face_mesh,arm_obj,sk_name,bone_name,loc_axis,expression,smin,smax):
    sk=face_mesh.data.shape_keys
    if not sk or sk_name not in sk.key_blocks: return
    sk.animation_data_create(); _remove_driver(sk,sk_name)
    kb=sk.key_blocks[sk_name]; kb.slider_min=smin; kb.slider_max=smax
    drv=kb.driver_add("value").driver; drv.type='SCRIPTED'
    v=drv.variables.new(); v.name,v.type="var",'TRANSFORMS'
    t=v.targets[0]; t.id,t.bone_target=arm_obj,bone_name
    t.transform_type=['LOC_X','LOC_Y','LOC_Z'][loc_axis]
    t.transform_space='LOCAL_SPACE'
    drv.expression=expression

def _setup_scale_driver(face_mesh,arm_obj,sk_name,loc_bone,expression):
    sk=face_mesh.data.shape_keys
    if not sk or sk_name not in sk.key_blocks: return
    sk.animation_data_create(); _remove_driver(sk,sk_name)
    drv=sk.key_blocks[sk_name].driver_add("value").driver; drv.type='SCRIPTED'
    v=drv.variables.new(); v.name,v.type="var",'TRANSFORMS'
    t=v.targets[0]; t.id,t.bone_target=arm_obj,loc_bone
    t.transform_type,t.transform_space='SCALE_AVG','LOCAL_SPACE'
    drv.expression=expression

def _split_bone_words(bone_name):
    spaced = re.sub(r'(?<=[a-z0-9])(?=[A-Z])', '_', bone_name)
    return [p for p in re.split(r'[_.\s]+', spaced.lower()) if p]

def _term_matches_prefix(bone_name, term):
    parts = _split_bone_words(bone_name)
    term_l = term.strip().lower()
    return any(part.startswith(term_l) for part in parts)

def _setup_bone_collections(arm_obj,bone_coll_prop,remove_from_main=True):
    arm=arm_obj.data; collections=arm.collections
    coll_dict={}
    for entry in bone_coll_prop:
        name=entry.coll_name.strip()
        terms=[t.strip() for t in entry.terms.split(",") if t.strip()]
        if name and terms: coll_dict[name]=terms
    coll_map={}
    for name in coll_dict:
        if name in collections: collections.remove(collections[name])
        coll_map[name]=collections.new(name)
    main_coll=collections.get("Main") if remove_from_main else None
    counts={name:0 for name in coll_dict}
    for bone in arm.bones:
        for cn,terms in coll_dict.items():
            if any(_term_matches_prefix(bone.name,t) for t in terms):
                coll_map[cn].assign(bone); counts[cn]+=1
                if main_coll:
                    try: main_coll.unassign(bone)
                    except Exception: pass
                break
    return counts


# ─────────────────────────────────────────────────────────────────────────────
#  PROPERTY GROUPS
# ─────────────────────────────────────────────────────────────────────────────

class UmaBoneCollEntry(PropertyGroup):
    coll_name: StringProperty(name="Name", default="New Collection")
    terms:     StringProperty(name="Keywords", default="keyword")
    count:     IntProperty(name="Bones Matched", default=-1)

_DEFAULT_COLLECTIONS = [
    ("Hair","hair, ear, tail"), ("Cloth","shirt, jacket, skirt, ribbon, mantle, cloth, acc, sleeve"),
    ("Physics","bust"), ("Face","cheek, nose"), ("Eyes","eye, eyebrow"), ("Mouth","mouth"),
]

class UmaRigProps(PropertyGroup):
    # Objects
    armature_obj:  PointerProperty(name="Armature",  type=bpy.types.Object, poll=_poll_armature)
    face_mesh_obj: PointerProperty(name="Face Mesh", type=bpy.types.Object, poll=_poll_mesh)
    shape_key_mesh:PointerProperty(name="Mesh",      type=bpy.types.Object, poll=_poll_mesh)
    hand_mesh_obj: PointerProperty(name="Body Mesh", type=bpy.types.Object, poll=_poll_mesh,
                                    description="Required. Mesh with vertex groups matching bone "
                                                "names — used to snap fingertip bones onto the mesh tip")

    # Section toggles
    show_skeleton_cleanup:  BoolProperty(default=False)
    show_rig_cleanup:       BoolProperty(default=False)
    show_eye_rig:           BoolProperty(default=False)
    show_bone_coll:         BoolProperty(default=False)
    show_shape_keys:        BoolProperty(default=False)
    show_advanced:          BoolProperty(default=False)

    # Eye rig drivers (limits removed)
    xrange_l_min:  FloatProperty(name="Min",default=-1.0,soft_min=-5.0,soft_max=0.0,step=10,precision=3)
    xrange_l_max:  FloatProperty(name="Max",default=1.4, soft_min=0.0, soft_max=5.0,step=10,precision=3)
    xrange_l_expr: StringProperty(name="Expression",default="var * -1.5",maxlen=256)
    xrange_r_min:  FloatProperty(name="Min",default=-0.4)
    xrange_r_max:  FloatProperty(name="Max",default=1.4)
    xrange_r_expr: StringProperty(name="Expression",default="var * -1.5",maxlen=256)
    yrange_l_min:  FloatProperty(name="Min",default=-2.0)
    yrange_l_max:  FloatProperty(name="Max",default=2.0)
    yrange_l_expr: StringProperty(name="Expression",default="var * -1.5",maxlen=256)
    yrange_r_min:  FloatProperty(name="Min",default=-2.0)
    yrange_r_max:  FloatProperty(name="Max",default=2.0)
    yrange_r_expr: StringProperty(name="Expression",default="var * 1.5",maxlen=256)

    close_l_min: FloatProperty(name="Closed", default=0.8)
    close_l_max: FloatProperty(name="Open",   default=1.0)
    close_r_min: FloatProperty(name="Closed", default=0.8)
    close_r_max: FloatProperty(name="Open",   default=1.0)

    odoroki_l_min: FloatProperty(name="Neutral", default=1.0)
    odoroki_l_max: FloatProperty(name="Wide",    default=1.2)
    odoroki_r_min: FloatProperty(name="Neutral", default=1.0)
    odoroki_r_max: FloatProperty(name="Wide",    default=1.2)

    bone_collections: CollectionProperty(type=UmaBoneCollEntry)
    bone_coll_active: IntProperty(default=0)
    eye_driver_active: IntProperty(default=0)


# ─────────────────────────────────────────────────────────────────────────────
#  OPERATORS
# ─────────────────────────────────────────────────────────────────────────────

def _get_arm(context):
    props = context.scene.uma_rig
    return props.armature_obj

def _require_arm(self, context):
    obj = _get_arm(context)
    if obj is None:
        self.report({'ERROR'}, "Select an Armature first."); return None
    return obj


class UMARIG_OT_run_finger_hand(Operator):
    bl_idname="uma_rig.run_finger_hand"; bl_label="Build Finger & Hand Controller"; bl_options={'REGISTER','UNDO'}
    def execute(self, context):
        obj = _require_arm(self, context)
        if obj is None: return {'CANCELLED'}
        props = context.scene.uma_rig
        if props.hand_mesh_obj is None:
            self.report({'ERROR'}, "Body Mesh is required to build the Finger & Hand Controller.")
            return {'CANCELLED'}
        try:
            bpy.context.view_layer.objects.active = obj
            run_finger_controller(obj, props.hand_mesh_obj)
            run_hand_controller(obj)
            self.report({'INFO'}, "Finger & Hand Controller built ✓")
        except Exception as e:
            self.report({'ERROR'}, str(e)); return {'CANCELLED'}
        return {'FINISHED'}


class UMARIG_OT_run_ear(Operator):
    bl_idname="uma_rig.run_ear"; bl_label="Build Ear Controller"; bl_options={'REGISTER','UNDO'}
    def execute(self, context):
        obj = _require_arm(self, context)
        if obj is None: return {'CANCELLED'}
        try:
            bpy.context.view_layer.objects.active = obj
            run_ear_controller(obj)
            self.report({'INFO'}, "Ear Controller built ✓")
        except Exception as e:
            self.report({'ERROR'}, str(e)); return {'CANCELLED'}
        return {'FINISHED'}


class UMARIG_OT_run_all(Operator):
    bl_idname="uma_rig.run_all"; bl_label="Build Fingers + Hands + Ears"; bl_options={'REGISTER','UNDO'}
    def execute(self, context):
        obj = _require_arm(self, context)
        if obj is None: return {'CANCELLED'}
        props = context.scene.uma_rig
        if props.hand_mesh_obj is None:
            self.report({'ERROR'}, "Body Mesh is required to build controllers.")
            return {'CANCELLED'}
        try:
            bpy.context.view_layer.objects.active = obj
            run_finger_controller(obj, props.hand_mesh_obj)
            run_hand_controller(obj)
            run_ear_controller(obj)
            self.report({'INFO'}, "All controllers built ✓")
        except Exception as e:
            self.report({'ERROR'}, str(e)); return {'CANCELLED'}
        return {'FINISHED'}


class UMARIG_OT_rig_cleanup(Operator):
    bl_idname="uma_rig.rig_cleanup"; bl_label="Cleanup Rig Controllers"; bl_options={'REGISTER','UNDO'}
    def execute(self, context):
        obj = _require_arm(self, context)
        if obj is None: return {'CANCELLED'}
        try:
            bpy.context.view_layer.objects.active = obj
            run_cleanup(obj)
            self.report({'INFO'}, "Rig cleanup done ✓")
        except Exception as e:
            self.report({'ERROR'}, str(e)); return {'CANCELLED'}
        return {'FINISHED'}


class UMARIG_OT_skeleton_cleanup(Operator):
    bl_idname="uma_rig.skeleton_cleanup"; bl_label="Clean Skeleton"; bl_options={'REGISTER','UNDO'}
    def execute(self, context):
        obj = _require_arm(self, context)
        if obj is None: return {'CANCELLED'}
        try:
            bpy.context.view_layer.objects.active = obj
            n = run_skeleton_cleanup(obj)
            self.report({'INFO'}, f"Skeleton cleanup: {n} bones removed ✓")
        except Exception as e:
            self.report({'ERROR'}, str(e)); return {'CANCELLED'}
        return {'FINISHED'}


class UMARIG_OT_shape_keys(Operator):
    bl_idname="uma_rig.shape_keys"; bl_label="Combine Shape Keys"; bl_options={'REGISTER','UNDO'}
    def execute(self, context):
        props = context.scene.uma_rig
        obj = props.shape_key_mesh
        if obj is None:
            self.report({'ERROR'}, "Select a Mesh with shape keys first.")
            return {'CANCELLED'}
        try:
            n = run_shape_keys_combiner(obj)
            self.report({'INFO'}, f"{n} combined shape key(s) created ✓")
        except Exception as e:
            self.report({'ERROR'}, str(e)); return {'CANCELLED'}
        return {'FINISHED'}


class UMARIG_OT_eye_run(Operator):
    bl_idname="uma_rig.eye_run"; bl_label="Build Eye Rig"; bl_options={'REGISTER','UNDO'}
    def execute(self, context):
        props=context.scene.uma_rig
        arm_obj=props.armature_obj; face_mesh=props.face_mesh_obj
        if arm_obj is None:
            self.report({'ERROR',"Select Armature first."}); return {'CANCELLED'}
        if face_mesh is None:
            self.report({'ERROR'},"Select Face Mesh first."); return {'CANCELLED'}
        try:
            bpy.context.view_layer.objects.active=arm_obj
            build_eye_rig_controller(context, arm_obj, props)
            p=props
            _setup_location_driver(face_mesh,arm_obj,SK_XRANGE_L,EYE_LOCATOR_L,0,p.xrange_l_expr,p.xrange_l_min,p.xrange_l_max)
            _setup_location_driver(face_mesh,arm_obj,SK_XRANGE_R,EYE_LOCATOR_R,0,p.xrange_r_expr,p.xrange_r_min,p.xrange_r_max)
            _setup_location_driver(face_mesh,arm_obj,SK_YRANGE_L,EYE_LOCATOR_L,2,p.yrange_l_expr,p.yrange_l_min,p.yrange_l_max)
            _setup_location_driver(face_mesh,arm_obj,SK_YRANGE_R,EYE_LOCATOR_R,2,p.yrange_r_expr,p.yrange_r_min,p.yrange_r_max)
            _setup_scale_driver(face_mesh,arm_obj,SK_CLOSE_L,EYE_LOCATOR_L,_build_close_expr(p.close_l_min,p.close_l_max))
            _setup_scale_driver(face_mesh,arm_obj,SK_CLOSE_R,EYE_LOCATOR_R,_build_close_expr(p.close_r_min,p.close_r_max))
            _setup_scale_driver(face_mesh,arm_obj,SK_ODOROKI_L,EYE_LOCATOR_L,_build_odoroki_expr(p.odoroki_l_min,p.odoroki_l_max))
            _setup_scale_driver(face_mesh,arm_obj,SK_ODOROKI_R,EYE_LOCATOR_R,_build_odoroki_expr(p.odoroki_r_min,p.odoroki_r_max))
            bpy.context.view_layer.update()
            self.report({'INFO'},"Eye Rig built ✓")
        except Exception as ex:
            try: bpy.ops.object.mode_set(mode='POSE')
            except Exception: pass
            self.report({'ERROR'},f"Setup failed: {ex}"); return {'CANCELLED'}
        return {'FINISHED'}


class UMARIG_OT_eye_reset(Operator):
    bl_idname="uma_rig.eye_reset"; bl_label="Reset Defaults"; bl_options={'REGISTER','UNDO'}
    def execute(self,context):
        p=context.scene.uma_rig
        p.xrange_l_min=-1.0; p.xrange_l_max=1.4; p.xrange_l_expr="var * -1.5"
        p.xrange_r_min=-0.4; p.xrange_r_max=1.4; p.xrange_r_expr="var * -1.5"
        p.yrange_l_min=-2.0; p.yrange_l_max=2.0; p.yrange_l_expr="var * -1.5"
        p.yrange_r_min=-2.0; p.yrange_r_max=2.0; p.yrange_r_expr="var * 1.5"
        p.close_l_min=0.8; p.close_l_max=1.0
        p.close_r_min=0.8; p.close_r_max=1.0
        p.odoroki_l_min=1.0; p.odoroki_l_max=1.2
        p.odoroki_r_min=1.0; p.odoroki_r_max=1.2
        self.report({'INFO'},"Defaults restored."); return {'FINISHED'}


class UMARIG_OT_eye_select(Operator):
    bl_idname="uma_rig.eye_select"; bl_label="Select Eye Driver"; bl_options={'INTERNAL'}
    index: IntProperty()
    def execute(self,context):
        context.scene.uma_rig.eye_driver_active=self.index
        return {'FINISHED'}


class UMARIG_OT_coll_add(Operator):
    bl_idname="uma_rig.coll_add"; bl_label="Add Collection"; bl_options={'REGISTER','UNDO'}
    def execute(self,context):
        props=context.scene.uma_rig; e=props.bone_collections.add()
        e.coll_name="New Collection"; e.terms="keyword"
        props.bone_coll_active=len(props.bone_collections)-1; return {'FINISHED'}

class UMARIG_OT_coll_remove(Operator):
    bl_idname="uma_rig.coll_remove"; bl_label="Remove Collection"; bl_options={'REGISTER','UNDO'}
    index: IntProperty()
    def execute(self,context):
        props=context.scene.uma_rig
        if 0<=self.index<len(props.bone_collections):
            props.bone_collections.remove(self.index)
        return {'FINISHED'}

class UMARIG_OT_coll_reset(Operator):
    bl_idname="uma_rig.coll_reset"; bl_label="Reset Collections"; bl_options={'REGISTER','UNDO'}
    def execute(self,context):
        props=context.scene.uma_rig; props.bone_collections.clear()
        for name,terms in _DEFAULT_COLLECTIONS:
            e=props.bone_collections.add(); e.coll_name=name; e.terms=terms
        return {'FINISHED'}

class UMARIG_OT_build_collections(Operator):
    bl_idname="uma_rig.build_collections"; bl_label="Build Bone Collections"; bl_options={'REGISTER','UNDO'}
    def execute(self,context):
        props=context.scene.uma_rig
        if props.armature_obj is None:
            self.report({'ERROR'},"No armature selected."); return {'CANCELLED'}
        try:
            counts=_setup_bone_collections(props.armature_obj,props.bone_collections,True)
            for entry in props.bone_collections:
                entry.count=counts.get(entry.coll_name.strip(),0)
            total=sum(counts.values())
            self.report({'INFO'},f"Collections built — {total} bones assigned across {len(counts)} collections.")
        except Exception as e:
            self.report({'ERROR'},str(e)); return {'CANCELLED'}
        return {'FINISHED'}

class UMARIG_OT_coll_move(Operator):
    bl_idname="uma_rig.coll_move"; bl_label="Move Collection"; bl_options={'REGISTER','UNDO'}
    direction: StringProperty(default='UP')
    def execute(self,context):
        props=context.scene.uma_rig
        idx=props.bone_coll_active
        new_idx=idx-1 if self.direction=='UP' else idx+1
        if 0<=new_idx<len(props.bone_collections):
            props.bone_collections.move(idx,new_idx)
            props.bone_coll_active=new_idx
        return {'FINISHED'}


# ─────────────────────────────────────────────────────────────────────────────
#  PANEL
# ─────────────────────────────────────────────────────────────────────────────

class UMARIG_UL_bone_collections(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        row = layout.row(align=True)
        split = row.split(factor=0.4, align=True)
        split.prop(item, "coll_name", text="", emboss=False, icon='GROUP_BONE')
        r2 = split.row(align=True)
        r2.prop(item, "terms", text="", emboss=False, icon='SORTALPHA')

        if item.count < 0:
            row.label(text="", icon='BLANK1')
        elif item.count == 0:
            r3 = row.row(); r3.alert = True
            r3.label(text="0", icon='ERROR')
        else:
            row.label(text=str(item.count), icon='CHECKMARK')

    def filter_items(self, context, data, propname):
        items = getattr(data, propname)
        flt_flags = [self.bitflag_filter_item] * len(items)
        flt_neworder = []
        if self.filter_name:
            flt_flags = bpy.types.UI_UL_list.filter_items_by_name(
                self.filter_name, self.bitflag_filter_item, items, "coll_name")
        return flt_flags, flt_neworder


def _section_header(layout, props, show_attr, label, icon):
    box = layout.box()
    row = box.row(align=True)
    row.prop(props, show_attr,
             icon='TRIA_DOWN' if getattr(props, show_attr) else 'TRIA_RIGHT',
             icon_only=True, emboss=False)
    row.label(text=label, icon=icon)
    return box, getattr(props, show_attr)


class UMARIG_PT_main(Panel):
    bl_label       = "Uma Rig Tools"
    bl_idname      = "UMARIG_PT_main"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category    = "Uma Rig"

    def draw(self, context):
        layout = self.layout
        props  = context.scene.uma_rig

        # Object pickers
        obj_box = layout.box()
        obj_box.label(text="Scene Objects", icon='SCENE_DATA')
        r=obj_box.row(align=True); r.alert=props.armature_obj is None
        r.prop(props,"armature_obj",text="Armature",icon='ARMATURE_DATA')

        layout.separator(factor=0.3)

        # Controllers section
        ctrl_box = layout.box()
        ctrl_box.label(text="Controllers", icon='HAND')
        ctrl_box.separator(factor=0.2)

        r=ctrl_box.row(align=True); r.alert=props.hand_mesh_obj is None
        r.prop(props,"hand_mesh_obj",text="Body Mesh *",icon='MESH_DATA')
        if props.hand_mesh_obj is None:
            warn=ctrl_box.row(); warn.alert=True
            warn.label(text="Body Mesh is required to build controllers", icon='ERROR')

        ap=_actions_path()
        info=ctrl_box.column(); info.enabled=False
        info.label(text=f"actions.py: {'✓ found' if ap.exists() else '✗ NOT FOUND'}",
                   icon='CHECKMARK' if ap.exists() else 'ERROR')

        ctrl_ready = props.armature_obj is not None and props.hand_mesh_obj is not None

        ctrl_box.separator(factor=0.3)
        r=ctrl_box.row(); r.scale_y=1.3
        r.enabled=ctrl_ready
        r.operator("uma_rig.run_finger_hand",icon='HAND',text="Build Finger & Hand Controller")
        r=ctrl_box.row(); r.scale_y=1.3
        r.enabled=ctrl_ready
        r.operator("uma_rig.run_ear",icon='OUTLINER_DATA_SPEAKER',text="Build Ear Controller")

        ctrl_box.separator(factor=0.3)
        r=ctrl_box.row(); r.scale_y=1.5
        r.enabled=ctrl_ready
        r.operator("uma_rig.run_all",icon='RENDER_ANIMATION',text="Build All Controllers")

        layout.separator(factor=0.3)

        # Skeleton Cleanup
        box, open_ = _section_header(layout, props, "show_skeleton_cleanup",
                                      "Skeleton Cleanup", 'TRASH')
        if open_:
            box.separator(factor=0.2)
            info=box.column(); info.enabled=False
            info.label(text="Removes: *handle  |  Sp_He_Ear0_*", icon='INFO')
            box.separator(factor=0.3)
            r=box.row(); r.scale_y=1.4
            r.enabled=props.armature_obj is not None
            r.operator("uma_rig.skeleton_cleanup",icon='TRASH',text="Clean Skeleton")

        layout.separator(factor=0.2)

        # Rig Cleanup
        box, open_ = _section_header(layout, props, "show_rig_cleanup",
                                      "Rig Cleanup", 'LOOP_BACK')
        if open_:
            box.separator(factor=0.2)
            info=box.column(); info.enabled=False
            info.label(text="Removes _roll bones, hand_control, actions, constraints",icon='INFO')
            box.separator(factor=0.3)
            r=box.row(); r.scale_y=1.4; r.alert=True
            r.enabled=props.armature_obj is not None
            r.operator("uma_rig.rig_cleanup",icon='CANCEL',text="Cleanup Rig Controllers")

        layout.separator(factor=0.4)

        # Eye Rig Setup (simplified, no limits)
        box, open_ = _section_header(layout, props, "show_eye_rig",
                                      "Eye Rig Setup", 'HIDE_OFF')
        if open_:
            box.separator(factor=0.2)
            r=box.row(align=True); r.alert=props.face_mesh_obj is None
            r.prop(props,"face_mesh_obj",text="Face Mesh",icon='MESH_DATA')

            box.separator(factor=0.3)
            box.label(text="Shape Key Drivers", icon='SHAPEKEY_DATA')

            # 2 drivers per row (they come pre-paired L/R in EYE_DRIVER_DEFS)
            list_box = box.box()
            for pair_start in range(0, len(EYE_DRIVER_DEFS), 2):
                pair_row = list_box.row(align=True)
                for offset in (0, 1):
                    idx = pair_start + offset
                    if idx >= len(EYE_DRIVER_DEFS):
                        break
                    d = EYE_DRIVER_DEFS[idx]
                    if d["kind"] == 'expr':
                        ok, msg = validate_expression(getattr(props, d["expr"]))
                    else:
                        ok = abs(getattr(props, d["max"]) - getattr(props, d["min"])) > 1e-6

                    cell = pair_row.row(align=True)
                    split = cell.split(factor=0.85, align=True)
                    op = split.operator("uma_rig.eye_select", text=d["label"], icon=d["icon"],
                                         depress=(idx == props.eye_driver_active))
                    op.index = idx
                    status = split.row(); status.alert = not ok
                    status.label(text="", icon='CHECKMARK' if ok else 'ERROR')

                    if offset == 0:
                        pair_row.separator(factor=0.4)

            active_idx=props.eye_driver_active
            if 0<=active_idx<len(EYE_DRIVER_DEFS):
                d=EYE_DRIVER_DEFS[active_idx]
                detail=box.box()
                detail.label(text=d["label"],icon=d["icon"])
                col=detail.column(align=True)
                r2=col.row(align=True)
                if d["kind"]=='expr':
                    r2.prop(props,d["min"],text="Min"); r2.prop(props,d["max"],text="Max")
                    detail.separator(factor=0.3)
                    detail.label(text="Driver Expression (var):",icon='DRIVER')
                    detail.prop(props,d["expr"],text="")
                    ok,msg=validate_expression(getattr(props,d["expr"]))
                    if not ok:
                        r3=detail.row(); r3.alert=True; r3.label(text=f"⚠  {msg}",icon='ERROR')
                else:
                    r2.prop(props,d["min"],text=d["min_label"])
                    r2.prop(props,d["max"],text=d["max_label"])
                    denom_ok=abs(getattr(props,d["max"])-getattr(props,d["min"]))>1e-6
                    if not denom_ok:
                        r3=detail.row(); r3.alert=True
                        r3.label(text=f"⚠  {d['min_label']} and {d['max_label']} must differ",icon='ERROR')
                    detail.separator(factor=0.2)
                    info2=detail.column(); info2.enabled=False
                    info2.label(text="Formula is auto-built from these two values",icon='INFO')

            box.separator(factor=0.2)
            info=box.column(); info.enabled=False
            info.label(text="✓ = valid   ⚠ = needs fixing",icon='INFO')

            box.separator(factor=0.3)
            box.operator("uma_rig.eye_reset",text="Reset Defaults",icon='LOOP_BACK')
            box.separator(factor=0.4)
            r=box.row(); r.scale_y=1.6
            r.enabled = props.armature_obj is not None and props.face_mesh_obj is not None
            r.operator("uma_rig.eye_run",icon='PLAY',text="Build Eye Rig")

        layout.separator(factor=0.4)

        # Bone Collections
        box, open_ = _section_header(layout, props, "show_bone_coll",
                                      "Bone Collections", 'GROUP_BONE')
        if open_:
            box.separator(factor=0.2)

            list_row = box.row()
            list_row.template_list(
                "UMARIG_UL_bone_collections", "", props, "bone_collections",
                props, "bone_coll_active", rows=5)

            side = list_row.column(align=True)
            side.operator("uma_rig.coll_add", text="", icon='ADD')
            op = side.operator("uma_rig.coll_remove", text="", icon='REMOVE')
            op.index = props.bone_coll_active
            side.separator()
            up = side.operator("uma_rig.coll_move", text="", icon='TRIA_UP')
            up.direction = 'UP'
            down = side.operator("uma_rig.coll_move", text="", icon='TRIA_DOWN')
            down.direction = 'DOWN'
            side.separator()
            side.operator("uma_rig.coll_reset", text="", icon='LOOP_BACK')

            if not props.bone_collections:
                box.label(text="No collections. Click + to add.", icon='INFO')
            elif 0 <= props.bone_coll_active < len(props.bone_collections):
                active = props.bone_collections[props.bone_coll_active]
                detail = box.box()
                detail.label(text="Selected Collection", icon='RESTRICT_SELECT_OFF')
                detail.prop(active, "coll_name", text="Name")
                detail.prop(active, "terms", text="Prefixes")
                if active.count == 0:
                    r = detail.row(); r.alert = True
                    r.label(text="No bones matched these prefixes yet.", icon='ERROR')

            box.separator(factor=0.3)
            info = box.column(); info.enabled = False
            info.label(text="✓ = bones assigned on last build   ⚠ = 0 matches", icon='INFO')
            box.separator(factor=0.2)
            r=box.row(); r.scale_y=1.4
            r.enabled=props.armature_obj is not None
            r.operator("uma_rig.build_collections",icon='OUTLINER_OB_ARMATURE',text="Build Collections")

        layout.separator(factor=0.4)

        # Shape Keys Combiner
        box, open_ = _section_header(layout, props, "show_shape_keys",
                                      "Shape Keys Combiner", 'SHAPEKEY_DATA')
        if open_:
            box.separator(factor=0.2)
            r=box.row(align=True); r.alert=props.shape_key_mesh is None
            r.prop(props,"shape_key_mesh",text="Mesh",icon='MESH_DATA')
            box.separator(factor=0.3)
            info=box.column(); info.enabled=False
            info.label(text="Combines _L + _R pairs into a single shape key",icon='INFO')
            box.separator(factor=0.3)
            r=box.row(); r.scale_y=1.4
            r.enabled=props.shape_key_mesh is not None
            r.operator("uma_rig.shape_keys",icon='PLAY',text="Combine Shape Keys")


# ─────────────────────────────────────────────────────────────────────────────
#  REGISTER
# ─────────────────────────────────────────────────────────────────────────────

_classes = (
    UmaBoneCollEntry, UmaRigProps,
    UMARIG_OT_run_finger_hand, UMARIG_OT_run_ear,
    UMARIG_OT_run_all, UMARIG_OT_rig_cleanup, UMARIG_OT_skeleton_cleanup,
    UMARIG_OT_shape_keys,
    UMARIG_OT_eye_run, UMARIG_OT_eye_reset, UMARIG_OT_eye_select,
    UMARIG_UL_bone_collections,
    UMARIG_OT_coll_add, UMARIG_OT_coll_remove, UMARIG_OT_coll_reset, UMARIG_OT_coll_move,
    UMARIG_OT_build_collections,
    UMARIG_PT_main,
)

def _seed_bone_collections(dummy=None):
    for scene in bpy.data.scenes:
        props=scene.uma_rig
        if len(props.bone_collections)==0:
            for name,terms in _DEFAULT_COLLECTIONS:
                e=props.bone_collections.add(); e.coll_name=name; e.terms=terms
    if _seed_bone_collections in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(_seed_bone_collections)

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.uma_rig=PointerProperty(type=UmaRigProps)
    bpy.app.handlers.depsgraph_update_post.append(_seed_bone_collections)

def unregister():
    if _seed_bone_collections in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(_seed_bone_collections)
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.uma_rig

if __name__=="__main__":
    register()