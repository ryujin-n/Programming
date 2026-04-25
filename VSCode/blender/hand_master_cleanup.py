import bpy

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


# ── Helpers ───────────────────────────────────────────────────────────────────

def is_roll_bone(name):   return "_roll" in name.lower()


def is_finger_bone_base(name):
    prefixes = ["c_thumb", "c_index", "c_middle", "c_ring", "c_pinky"]
    sides = [".l", ".r"]
    lower = name.lower()
    return (any(lower.startswith(p) for p in prefixes)
            and any(lower.endswith(s) for s in sides))


# ── Cleanup ───────────────────────────────────────────────────────────────────

def run():
    obj = bpy.context.active_object
    if obj is None or obj.type != 'ARMATURE':
        raise RuntimeError("Select an Armature before running the cleanup script.")

    arm = obj.data

    # ── 1. Remove action constraints + finger bones drivers   ────────────
    bpy.ops.object.mode_set(mode='POSE')
    removed_constraints = 0
    removed_drivers = 0

    for pb in obj.pose.bones:
        # Remove Action constraints
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

        # Remove Copy Rotation
        if is_finger_bone_base(pb.name) or is_roll_bone(pb.name):
            for c in list(pb.constraints):
                if c.type == "COPY_ROTATION":
                    pb.constraints.remove(c)
                    removed_constraints += 1

        # Remove Limit constraints
        if pb.name in HAND_CONTROL_BONES:
            for c in list(pb.constraints):
                if c.type in HAND_CTRL_CONSTRAINT_TYPES:
                    pb.constraints.remove(c)
                    removed_constraints += 1

    print(f"  [cleanup] Constraints removidas : {removed_constraints}")
    print(f"  [cleanup] Drivers removidos      : {removed_drivers}")

    # ── 2. Remove bones _roll and hand_control  ────────────────────
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

    # ── 3. Remove Bone Collection _roll_hidden ────────────────────────────────
    coll = arm.collections.get(HIDDEN_COLL_NAME)
    if coll:
        arm.collections.remove(coll)
        print(f"  [cleanup] Bone Collection '{HIDDEN_COLL_NAME}' removida.")

    # ── 4. Remove Actions ──────────────
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


run()