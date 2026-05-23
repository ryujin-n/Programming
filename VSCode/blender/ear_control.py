import bpy
import re

# ═══════════════════════════════════════════════════════════════════════════════
#  CONFIGURAÇÃO
# ═══════════════════════════════════════════════════════════════════════════════

EAR_PREFIX = "Ear_"        # prefixo dos bones de orelha
SIDES      = ["_L", "_R"]  # sufixos laterais


# ═══════════════════════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

def split_ear_side(name: str):
    """
    Separa o sufixo lateral do restante.
    Ex.: 'Ear_01_L'  →  ('Ear_01', '_L')
         'Ear_03_R'  →  ('Ear_03', '_R')
    """
    for side in SIDES:
        if name.endswith(side):
            return name[:-len(side)], side
    return name, None


def is_ear_bone(name: str) -> bool:
    """True para bones Ear_NN_L/R sem _roll."""
    if "_roll" in name.lower():
        return False
    base, side = split_ear_side(name)
    if side is None:
        return False
    return base.startswith(EAR_PREFIX)


def make_ear_roll_name(original: str) -> str:
    """
    Insere '_roll' antes do sufixo lateral.
    Ex.: 'Ear_01_L'  →  'Ear_01_roll_L'
    """
    base, side = split_ear_side(original)
    return (base + "_roll" + side) if side else (original + "_roll")


def segment_key(name: str) -> int:
    base, _ = split_ear_side(name)
    nums = re.findall(r'\d+', base)
    return int(nums[-1]) if nums else 0


# ═══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def run():
    obj = bpy.context.active_object
    if obj is None or obj.type != 'ARMATURE':
        raise RuntimeError("Select an Armature before running the script.")

    arm = obj.data
    bpy.ops.object.mode_set(mode='EDIT')
    edit_bones = arm.edit_bones

    # ── 1. Coleta e agrupa bones de orelha ───────────────────────────────────
    ear_names = [b.name for b in edit_bones if is_ear_bone(b.name)]

    if not ear_names:
        bpy.ops.object.mode_set(mode='POSE')
        raise RuntimeError(
            "No ear bones found. "
            "Check naming: Ear_NN_L / Ear_NN_R"
        )

    groups = {side: [] for side in SIDES}
    for name in ear_names:
        _, side = split_ear_side(name)
        if side:
            groups[side].append(name)
    for side in groups:
        groups[side].sort(key=segment_key)

    print(f"\n[ear_roll] Ear bones found:")
    for side, names in groups.items():
        print(f"  {side}: {names}")

    # ── 2. Mapeia original → roll ─────────────────────────────────────────────
    roll_map = {}
    for side, sorted_names in groups.items():
        for src_name in sorted_names:
            roll_map[src_name] = make_ear_roll_name(src_name)

    # ── 3. Cria edit_bones ────────────────────────────────────────────────────
    for src_name, roll_name in roll_map.items():
        if roll_name in edit_bones:
            print(f"  [skip] '{roll_name}' already exists.")
            continue

        src      = edit_bones[src_name]
        new_bone = edit_bones.new(roll_name)
        new_bone.head        = src.head.copy()
        new_bone.tail        = src.tail.copy()
        new_bone.matrix      = src.matrix.copy()
        new_bone.roll        = src.roll
        new_bone.use_connect = False

        print(f"  [ear_roll] Created: {roll_name}")

    # ── 4. Parenting ─────────────────────────────────────────────────────────
    #
    #   Ear_01_roll_L  →  Ear_01_L          ← ancora no bone original
    #   Ear_02_roll_L  →  Ear_01_roll_L
    #   Ear_03_roll_L  →  Ear_02_roll_L
    #
    for side, sorted_names in groups.items():
        for i, src_name in enumerate(sorted_names):
            roll_name = roll_map[src_name]
            if roll_name not in edit_bones:
                continue
            roll_bone = edit_bones[roll_name]
            if i == 0:
                # roll[0] → parent: head.x (independente do lado)
                if "head.x" in edit_bones:
                    roll_bone.parent = edit_bones["head.x"]
                else:
                    print(f"  [ear_roll] 'head.x' not found — {roll_name} created without parent.")
                roll_bone.use_connect = False
            else:
                prev_roll = roll_map[sorted_names[i - 1]]
                if prev_roll in edit_bones:
                    roll_bone.parent      = edit_bones[prev_roll]
                    roll_bone.use_connect = False

    # ── 5. Volta para Pose Mode ───────────────────────────────────────────────
    bpy.ops.object.mode_set(mode='POSE')

    # ── 6. Copy Rotation: roll[i] → roll[i-1]  (Replace) ────────────────────
    #
    #   Ear_01_roll_L  →  (sem constraint)
    #   Ear_02_roll_L  →  Copy Rotation de Ear_01_roll_L
    #   Ear_03_roll_L  →  Copy Rotation de Ear_02_roll_L
    #
    for side, sorted_names in groups.items():
        roll_chain = [roll_map[n] for n in sorted_names if roll_map.get(n) in obj.pose.bones]

        for i in range(1, len(roll_chain)):        # começa em 1, pula o [0]
            src_pb   = obj.pose.bones[roll_chain[i]]
            tgt_name = roll_chain[i - 1]

            # Remove duplicata
            for c in list(src_pb.constraints):
                if c.type == "COPY_ROTATION" and c.subtarget == tgt_name:
                    src_pb.constraints.remove(c)

            con = src_pb.constraints.new("COPY_ROTATION")
            con.target       = obj
            con.subtarget    = tgt_name
            con.mix_mode     = "REPLACE"
            con.target_space = "LOCAL_OWNER_ORIENT"
            con.owner_space  = "LOCAL"

            print(f"  [ear_roll] {roll_chain[i]}  →  Copy Rotation de {tgt_name}")

    # ── 7. Copy Rotation: original → seu _roll  (Add) ───────────────────────
    #
    #   Ear_01_L  →  Copy Rotation de Ear_01_roll_L  (Add)
    #   Ear_02_L  →  Copy Rotation de Ear_02_roll_L  (Add)
    #   Ear_03_L  →  Copy Rotation de Ear_03_roll_L  (Add)
    #
    for side, sorted_names in groups.items():
        for src_name in sorted_names:
            roll_name = roll_map.get(src_name)
            if not roll_name or src_name not in obj.pose.bones:
                continue

            pb = obj.pose.bones[src_name]

            # Remove duplicata
            for c in list(pb.constraints):
                if c.type == "COPY_ROTATION" and c.subtarget == roll_name:
                    pb.constraints.remove(c)

            con = pb.constraints.new("COPY_ROTATION")
            con.target       = obj
            con.subtarget    = roll_name
            con.mix_mode     = "ADD"
            con.target_space = "LOCAL_OWNER_ORIENT"
            con.owner_space  = "LOCAL"

            print(f"  [ear_roll] {src_name}  →  Copy Rotation de {roll_name}  (Add)")

    # ── 8. Widget "Roll 1" no roll[0] ────────────────────────────────────────
    import math

    for side, sorted_names in groups.items():
        roll_zero = roll_map.get(sorted_names[0])
        if not roll_zero or roll_zero not in obj.pose.bones:
            continue

        pb = obj.pose.bones[roll_zero]
        bpy.ops.pose.select_all(action='DESELECT')
        pb.select = True
        obj.data.bones.active = pb.bone

        try:
            # Espelha X e Z para o lado _R
            mirror = -1 if side == "_R" else 1
            bpy.context.window_manager.widget_list = "Roll 1"
            with bpy.context.temp_override(
                active_object=obj, object=obj,
                active_pose_bone=pb, selected_pose_bones=[pb],
            ):
                bpy.ops.bonewidget.create_widget(
                    relative_size      = True,
                    global_size_simple = 1.00,
                    slide_simple       = 0.00,
                    wireframe_width    = 2.00,
                )
            print(f"  [ear_roll] Widget 'Roll 1' → {roll_zero}  (mirror={mirror})")
        except Exception as e:
            print(f"  [ear_roll] Widget error '{roll_zero}': {e}")

    # ── 9. Esconde roll[1] e roll[2] via Bone Collection ────────────────────
    HIDDEN_COLL = "_roll_hidden"
    coll = arm.collections.get(HIDDEN_COLL) or arm.collections.new(HIDDEN_COLL)
    coll.is_visible = False

    for side, sorted_names in groups.items():
        roll_chain = [roll_map[n] for n in sorted_names if roll_map.get(n)]
        for bone_name in roll_chain[1:]:   # pula [0], esconde o resto
            bone = arm.bones.get(bone_name)
            if bone:
                coll.assign(bone)
                print(f"  [ear_roll] Hidden: {bone_name}")

    # ── Log ───────────────────────────────────────────────────────────────────
    print(f"\n[ear_roll] Parenting:")
    for side, sorted_names in groups.items():
        print(f"\n  [{side}]")
        for i, src_name in enumerate(sorted_names):
            roll_name    = roll_map[src_name]
            parent_label = src_name if i == 0 else roll_map[sorted_names[i - 1]]
            print(f"    {roll_name}  →  {parent_label}")

    print(f"\n[ear_roll] Done! {len(roll_map)} roll bones created/verified.")


run()