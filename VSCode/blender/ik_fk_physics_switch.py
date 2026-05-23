import bpy

rig    = bpy.data.objects["rig"]
c_traj = rig.pose.bones["c_traj"]


# ═══════════════════════════════════════════════════════════════════
# IK / FK SWITCHES
# ═══════════════════════════════════════════════════════════════════

ik_props = [
    {"prop_name": "IK_SWITCH_ARM_L", "target_bone": "c_hand_ik.l"},
    {"prop_name": "IK_SWITCH_ARM_R", "target_bone": "c_hand_ik.r"},
    {"prop_name": "IK_SWITCH_LEG_L", "target_bone": "c_foot_ik.l"},
    {"prop_name": "IK_SWITCH_LEG_R", "target_bone": "c_foot_ik.r"},
]

for p in ik_props:
    prop_name   = p["prop_name"]
    target_bone = p["target_bone"]

    c_traj[prop_name] = 0.0
    c_traj.id_properties_ui(prop_name).update(
        default=0.0,
        min=0.0, max=1.0,
        soft_min=0.0, soft_max=1.0,
        step=1,
        description=f"IK/FK switch for {target_bone}",
    )

    data_path = f'pose.bones["{target_bone}"]["ik_fk_switch"]'
    rig.driver_remove(data_path)

    drv = rig.driver_add(data_path).driver
    drv.type = 'SCRIPTED'

    var = drv.variables.new()
    var.name   = "ik_switch"
    var.type   = 'SINGLE_PROP'
    var.targets[0].id_type   = 'OBJECT'
    var.targets[0].id        = rig
    var.targets[0].data_path = f'pose.bones["c_traj"]["{prop_name}"]'

    drv.expression = "ik_switch"
    print(f"[OK] {prop_name}  ->  {target_bone}[ik_fk_switch]")


# ═══════════════════════════════════════════════════════════════════
# PHYSICS ON/OFF
# ═══════════════════════════════════════════════════════════════════

c_traj["PHYSICS_ON/OFF"] = 1
c_traj.id_properties_ui("PHYSICS_ON/OFF").update(
    default=1,
    min=0, max=1,
    soft_min=0, soft_max=1,
    step=1,
    description="Enable/Disable all physics (BoneX influence + GooPhysics)",
)
print("[OK] PHYSICS_ON/OFF created on c_traj")

# -- BoneX: driver on the influence of every constraint named *bonex_driver* --
bonex_count = 0
for bone in rig.pose.bones:
    for constraint in bone.constraints:
        if "bonex_driver" not in constraint.name.lower():
            continue

        data_path = (
            f'pose.bones["{bone.name}"]'
            f'.constraints["{constraint.name}"].influence'
        )
        rig.driver_remove(data_path)

        drv = rig.driver_add(data_path).driver
        drv.type = 'SCRIPTED'

        var = drv.variables.new()
        var.name   = "physics_toggle"
        var.type   = 'SINGLE_PROP'
        var.targets[0].id_type   = 'OBJECT'
        var.targets[0].id        = rig
        var.targets[0].data_path = 'pose.bones["c_traj"]["PHYSICS_ON/OFF"]'

        drv.expression = "physics_toggle"
        bonex_count += 1
        print(f"  [bonex] influence driver -> {bone.name} / {constraint.name}")

print(f"[OK] {bonex_count} bonex_driver constraint(s) found and driven")



print("\ndone -- all custom properties and drivers created on c_traj")