import bpy
import math
import pathlib


# ─────────────────────────────────────────────
#  CONFIGURAÇÃO — bones
# ─────────────────────────────────────────────

HEAD_POS = (0.52505, 0.052733, 1.2746)
TAIL_POS = (0.52505, 0.052733, 1.3046)

BONE_CONFIGS = [
    ("_L", ".l",  1),
    ("_R", ".r", -1),
]

BONE_BASE_NAME = "hand_control"

WIDGET_SHAPE      = "Root 1"
WIDGET_ROT_X      = math.radians(0)
WIDGET_ROT_Y      = math.radians(90)
WIDGET_ROT_Z      = math.radians(90)
WIDGET_WIRE_WIDTH = 2.00

# ─────────────────────────────────────────────
#  CONFIGURAÇÃO — actions
# ─────────────────────────────────────────────

ACTIONS_PATH       = pathlib.Path(
    r"C:\Users\miles\Documents\GitHub\Programming\VSCode\blender\actions.py"
)
OVERWRITE_EXISTING = False
USE_FAKE_USER      = True


# ─────────────────────────────────────────────
#  MAPA DE ACTION CONSTRAINTS
# ─────────────────────────────────────────────

def P(action, constraint, expr, ttype, rot_mode=None):
    return dict(action=action, constraint=constraint,
                expr=expr, type=ttype, rot_mode=rot_mode)

ACTION_CONSTRAINT_MAP = {

    ".l": {
        "ctrl": "hand_control_L",
        "groups": [
            {
                "bones": [
                    "c_pinky1_roll", "c_ring1_roll",
                    "c_middle1_roll", "c_index1_roll",
                    "c_thumb2_roll",
                ],
                "pairs": [
                    P("fist.l",   "Action_fist.l",   "max(0.0, min(1.0, var / -0.03))",  "LOC_X"),
                    P("extend.l", "Action_extend.l",  "max(0.0, min(1.0, var /  0.03))",  "LOC_X"),
                ],
            },
            {
                "bones": ["c_thumb1"],
                "pairs": [
                    P("fist.l",      "Action_fist.l",      "max(0.0, min(1.0, var / -0.03))",         "LOC_X"),
                    P("extend.l",    "Action_extend.l",    "max(0.0, min(1.0, var /  0.03))",         "LOC_X"),
                    P("roll.l",      "Action_roll.l",      "max(0.0, min(1.0, var / -0.500))",        "ROT_X", "QUATERNION"),
                    P("roll2.l",     "Action_roll2.l",     "max(0.0, min(1.0, var /  0.500))",        "ROT_X", "QUATERNION"),
                    P("adduction.l", "Action_adduction.l", "max(0.0, min(1.0, (var - 1.0) / -0.4))", "SCALE_Z"),
                    P("abduction.l", "Action_abduction.l", "max(0.0, min(1.0, (var - 1.0) /  0.3))", "SCALE_Z"),
                ],
            },
            {
                "bones": ["c_index1", "c_middle1", "c_ring1", "c_pinky1"],
                "pairs": [
                    P("roll.l",      "Action_roll.l",      "max(0.0, min(1.0, var / -0.500))",        "ROT_X", "QUATERNION"),
                    P("roll2.l",     "Action_roll2.l",     "max(0.0, min(1.0, var /  0.500))",        "ROT_X", "QUATERNION"),
                    P("adduction.l", "Action_adduction.l", "max(0.0, min(1.0, (var - 1.0) / -0.4))", "SCALE_Z"),
                    P("abduction.l", "Action_abduction.l", "max(0.0, min(1.0, (var - 1.0) /  0.3))", "SCALE_Z"),
                ],
            },
            {
                "bones": [
                    "c_index2", "c_index3",
                    "c_middle2", "c_middle3",
                    "c_ring2",   "c_ring3",
                    "c_pinky2",  "c_pinky3",
                    "c_thumb3",
                ],
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
                "bones": [
                    "c_pinky1_roll", "c_ring1_roll",
                    "c_middle1_roll", "c_index1_roll",
                    "c_thumb2_roll",
                ],
                "pairs": [
                    P("fist.r",   "Action_fist.r",   "max(0.0, min(1.0, var /  0.03))",  "LOC_X"),
                    P("extend.r", "Action_extend.r",  "max(0.0, min(1.0, var / -0.03))",  "LOC_X"),
                ],
            },
            {
                "bones": ["c_thumb1"],
                "pairs": [
                    P("fist.r",      "Action_fist.r",      "max(0.0, min(1.0, var /  0.03))",         "LOC_X"),
                    P("extend.r",    "Action_extend.r",    "max(0.0, min(1.0, var / -0.03))",         "LOC_X"),
                    P("roll.r",      "Action_roll.r",      "max(0.0, min(1.0, var /  0.500))",        "ROT_X", "QUATERNION"),
                    P("roll2.r",     "Action_roll2.r",     "max(0.0, min(1.0, var / -0.500))",        "ROT_X", "QUATERNION"),
                    P("adduction.r", "Action_adduction.r", "max(0.0, min(1.0, (var - 1.0) /  -0.4))", "SCALE_Z"),
                    P("abduction.r", "Action_abduction.r", "max(0.0, min(1.0, (var - 1.0) / 0.3))", "SCALE_Z"),
                ],
            },
            {
                "bones": ["c_index1", "c_middle1", "c_ring1", "c_pinky1"],
                "pairs": [
                    P("roll.r",      "Action_roll.r",      "max(0.0, min(1.0, var / -0.500))",        "ROT_X", "QUATERNION"),
                    P("roll2.r",     "Action_roll2.r",     "max(0.0, min(1.0, var /  0.500))",        "ROT_X", "QUATERNION"),
                    P("adduction.r", "Action_adduction.r", "max(0.0, min(1.0, (var - 1.0) /  -0.4))", "SCALE_Z"),
                    P("abduction.r", "Action_abduction.r", "max(0.0, min(1.0, (var - 1.0) / 0.3))", "SCALE_Z"),
                ],
            },
            {
                "bones": [
                    "c_index2", "c_index3",
                    "c_middle2", "c_middle3",
                    "c_ring2",   "c_ring3",
                    "c_pinky2",  "c_pinky3",
                    "c_thumb3",
                ],
                "pairs": [
                    P("claw.r", "Action_claw.r", "max(0.0, min(1.0, (var - 1.0) / -0.4))", "SCALE_X"),
                ],
            },
        ],
    },
}


# ─────────────────────────────────────────────
#  UTILS
# ─────────────────────────────────────────────

def safe_set(obj, attr, value):
    if hasattr(obj, attr):
        try:
            setattr(obj, attr, value)
        except Exception as e:
            print(f"  [warn] {attr} = {value!r} → {e}")
    else:
        print(f"  [warn] '{attr}' não existe nesta versão do Blender — pulado.")


# ─────────────────────────────────────────────
#  FUNÇÕES — actions
# ─────────────────────────────────────────────

def load_actions_data(filepath):
    filepath = pathlib.Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"[actions] Arquivo não encontrado: {filepath}")
    namespace = {}
    exec(filepath.read_text(encoding="utf-8"), namespace)
    if "ACTIONS_DATA" not in namespace:
        raise KeyError("[actions] ACTIONS_DATA não encontrado no arquivo.")
    return namespace["ACTIONS_DATA"]


def recreate_actions(actions_data, overwrite=OVERWRITE_EXISTING, fake_user=USE_FAKE_USER):
    created = []
    skipped = []

    for action_data in actions_data:
        name = action_data.get("name", "<sem nome>")

        if name in bpy.data.actions:
            if not overwrite:
                print(f"  [actions] Já existe, pulando: {name}")
                skipped.append(name)
                continue
            bpy.data.actions.remove(bpy.data.actions[name])

        action = bpy.data.actions.new(name)

        for fc_data in action_data.get("fcurves", []):
            try:
                fc = action.fcurves.new(
                    data_path    = fc_data["data_path"],
                    index        = fc_data["array_index"],
                    action_group = fc_data.get("group") or "",
                )
            except Exception as e:
                print(f"  [actions] F-Curve erro '{fc_data['data_path']}': {e}")
                continue

            fc.extrapolation = fc_data.get("extrapolation", "CONSTANT")
            keyframes = fc_data.get("keyframes", [])
            if not keyframes:
                continue

            fc.keyframe_points.add(len(keyframes))
            fc.keyframe_points.foreach_set("co",           [v for kp in keyframes for v in kp["co"]])
            fc.keyframe_points.foreach_set("handle_left",  [v for kp in keyframes for v in kp["handle_left"]])
            fc.keyframe_points.foreach_set("handle_right", [v for kp in keyframes for v in kp["handle_right"]])

            for i, kp_data in enumerate(keyframes):
                kp = fc.keyframe_points[i]
                kp.handle_left_type  = kp_data.get("handle_left_type",  "AUTO")
                kp.handle_right_type = kp_data.get("handle_right_type", "AUTO")
                kp.interpolation     = kp_data.get("interpolation", "BEZIER")
                kp.easing            = kp_data.get("easing", "AUTO")

            fc.update()

        # Slots (Blender 4.4+) — define display name como 'rig'
        if hasattr(action, 'slots'):
            for slot in action.slots:
                safe_set(slot, 'name_display', 'rig')

        action.use_fake_user = fake_user
        created.append(name)
        print(f"  [actions] Criada: {name}  ({len(action.fcurves)} F-Curves)")

    print(f"\n[actions] Criadas: {len(created)}  Puladas: {len(skipped)}")
    return created


# ─────────────────────────────────────────────
#  FUNÇÕES — action constraints
# ─────────────────────────────────────────────

def make_action_constraint(pb, armature_obj, action, constr_name,
                           expr, transform_type, rotation_mode=None,
                           hand_control_bone=None):
    if constr_name in pb.constraints:
        pb.constraints.remove(pb.constraints[constr_name])

    con = pb.constraints.new('ACTION')
    con.name      = constr_name
    con.target    = armature_obj
    con.subtarget = ""
    con.action    = action

    if hasattr(action, 'slots') and action.slots and hasattr(con, 'slot'):
        try:
            con.slot = action.slots[0]
        except Exception:
            pass

    safe_set(con, 'frame_start', 0)
    safe_set(con, 'frame_end',   10)
    con.influence = 1.0

    for mix_val in ('BEFORE_SPLIT', 'BEFORE'):
        try:
            con.mix_mode = mix_val
            break
        except (TypeError, AttributeError):
            continue

    safe_set(con, 'use_split_channels', True)

    for channel_val in ('LOCATION_X', 'LOC_X'):
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

    for attr in ('use_evaluation_time', 'use_eval_time', 'eval_time_type'):
        if hasattr(con, attr):
            try:
                setattr(con, attr, True)
                break
            except Exception:
                continue

    if expr and hand_control_bone:
        bone_name   = pb.name
        driver_path = f'pose.bones["{bone_name}"].constraints["{constr_name}"].eval_time'

        try:
            armature_obj.driver_remove(driver_path)
        except Exception:
            pass

        try:
            fc_drv = armature_obj.driver_add(driver_path)
            drv    = fc_drv.driver
            drv.type       = 'SCRIPTED'
            drv.expression = expr

            for v in list(drv.variables):
                drv.variables.remove(v)

            v = drv.variables.new()
            v.name = 'var'
            v.type = 'TRANSFORMS'
            tgt = v.targets[0]
            tgt.id              = armature_obj
            tgt.bone_target     = hand_control_bone
            tgt.transform_type  = transform_type
            tgt.transform_space = 'LOCAL_SPACE'

            if rotation_mode and hasattr(tgt, 'rotation_mode'):
                try:
                    tgt.rotation_mode = rotation_mode
                except Exception as e:
                    print(f"  [driver] rotation_mode erro: {e}")

            print(f"  [driver] {bone_name} / {constr_name}  [{transform_type}]  →  {expr}")

        except Exception as e:
            print(f"  [driver] Erro em '{constr_name}' ({bone_name}): {e}")

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
                    print(f"  [action_constraints] Bone '{full_name}' não encontrado — pulado.")
                    continue

                for pair in group["pairs"]:
                    action = bpy.data.actions.get(pair["action"])
                    if action is None:
                        print(f"  [action_constraints] Action '{pair['action']}' não encontrada — pulando {full_name}.")
                        continue

                    constr_name = pair["constraint"]

                    make_action_constraint(
                        pb                = pb,
                        armature_obj      = armature_obj,
                        action            = action,
                        constr_name       = constr_name,
                        expr              = pair["expr"],
                        transform_type    = pair["type"],
                        rotation_mode     = pair.get("rot_mode"),
                        hand_control_bone = ctrl_bone,
                    )
                    print(f"  [action_constraints] {full_name}  ←  {constr_name}")


# ─────────────────────────────────────────────
#  EXECUÇÃO PRINCIPAL
# ─────────────────────────────────────────────

def run():
    obj = bpy.context.active_object
    if obj is None or obj.type != 'ARMATURE':
        raise RuntimeError("Selecione uma Armature antes de executar o script.")

    arm = obj.data

    # ── 1. Edit Mode: cria bones ──────────────────────────────────────────────
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones    = arm.edit_bones
    created_bones = []

    for bone_suffix, parent_suffix, x_sign in BONE_CONFIGS:
        bone_name   = BONE_BASE_NAME + bone_suffix
        parent_name = "hand" + parent_suffix

        if bone_name in edit_bones:
            edit_bones.remove(edit_bones[bone_name])

        eb = edit_bones.new(bone_name)
        eb.head        = (HEAD_POS[0] * x_sign, HEAD_POS[1], HEAD_POS[2])
        eb.tail        = (TAIL_POS[0] * x_sign, TAIL_POS[1], TAIL_POS[2])
        eb.use_connect = False

        if parent_name in edit_bones:
            eb.parent = edit_bones[parent_name]
            print(f"  [hand_control] {bone_name} → parent: {parent_name}")
        else:
            print(f"  [hand_control] Parent '{parent_name}' não encontrado.")

        created_bones.append(bone_name)

    # ── 2. Pose Mode: locks + widget + limit constraints ──────────────────────
    bpy.ops.object.mode_set(mode='POSE')

    for bone_name in created_bones:
        pb = obj.pose.bones.get(bone_name)
        if pb is None:
            continue

        pb.lock_location = (False, True, True)
        pb.lock_scale    = (False, True, False)
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
            print(f"  [hand_control] Widget '{WIDGET_SHAPE}' → {bone_name}")
        except Exception as e:
            print(f"  [hand_control] Erro widget em {bone_name}: {e}")

        for c in list(pb.constraints):
            if c.type in ("LIMIT_LOCATION", "LIMIT_ROTATION", "LIMIT_SCALE"):
                pb.constraints.remove(c)

        ll = pb.constraints.new("LIMIT_LOCATION")
        ll.use_min_x = True;  ll.min_x = -0.03
        ll.use_min_y = True;  ll.min_y = -0.05
        ll.use_min_z = False
        ll.use_max_x = True;  ll.max_x =  0.03
        ll.use_max_y = True;  ll.max_y =  0.05
        ll.use_max_z = False
        ll.use_transform_limit = True
        ll.owner_space = 'LOCAL';  ll.influence = 1.0

        lr = pb.constraints.new("LIMIT_ROTATION")
        lr.use_limit_x = True
        lr.min_x = math.radians(-35);  lr.max_x = math.radians(35)
        lr.use_limit_y = False;  lr.use_limit_z = False
        lr.euler_order = 'AUTO'
        lr.use_transform_limit = True
        lr.owner_space = 'LOCAL';  lr.influence = 1.0
        safe_set(lr, 'use_legacy_behavior', True)

        ls = pb.constraints.new("LIMIT_SCALE")
        ls.use_min_x = True;  ls.min_x = 0.6
        ls.use_min_y = False
        ls.use_min_z = True;  ls.min_z = 0.6
        ls.use_max_x = True;  ls.max_x = 1.0
        ls.use_max_y = False
        ls.use_max_z = True;  ls.max_z = 1.3
        ls.use_transform_limit = True
        ls.owner_space = 'LOCAL';  ls.influence = 1.0

        print(f"  [hand_control] Constraints → {bone_name}")

    # ── 3. Actions ────────────────────────────────────────────────────────────
    actions_data = load_actions_data(ACTIONS_PATH)
    recreate_actions(actions_data)

    # ── 4. Action Constraints + Drivers ──────────────────────────────────────
    add_action_constraints(obj)

    print(f"\n[hand_control] Concluído! Bones: {created_bones}")


run()