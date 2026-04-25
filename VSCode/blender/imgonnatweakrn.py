"""
===============================================================
  UmaMusume Eye Rig Auto-Setup — Blender Panel Addon
  For use with UmaViewer exports + AutoRigPro + MMD Tools
===============================================================

INSTALLATION:
  1. Edit > Preferences > Add-ons > Install
  2. Select this .py file
  3. Enable "Rigging: UmaMusume Eye Rig Panel"
  4. In the 3D Viewport press N -> "Uma Eye Rig" tab
"""

bl_info = {
    "name":        "UmaMusume Eye Rig Panel",
    "author":      "Auto-generated",
    "version":     (1, 4, 0),
    "blender":     (4, 0, 0),
    "location":    "View3D > N-Panel > Uma Eye Rig",
    "description": "GUI panel to configure and run the UmaMusume eye rig auto-setup",
    "category":    "Rigging",
}

import bpy
import mathutils
import re
from bpy.types import Panel, Operator, PropertyGroup, UIList
from bpy.props import (StringProperty, FloatProperty, BoolProperty,
                        PointerProperty, CollectionProperty, IntProperty)


# ─────────────────────────────────────────────────────────────────────────────
#  POLL FUNCTIONS  (must be module-level for PointerProperty)
# ─────────────────────────────────────────────────────────────────────────────

def _poll_armature(self, obj):
    return obj.type == 'ARMATURE'

def _poll_mesh(self, obj):
    return obj.type == 'MESH'


# ─────────────────────────────────────────────────────────────────────────────
#  VALIDATION HELPERS
# ─────────────────────────────────────────────────────────────────────────────

ALLOWED_EXPR_CHARS = re.compile(r'^[0-9a-zA-Z_\+\-\*/\(\)\.\,\s<>=!&|%^~]+$')
DANGEROUS_KEYWORDS = ("import", "exec", "eval", "open", "os", "__", "globals",
                      "locals", "getattr", "setattr", "delattr", "compile",
                      "input", "print", "exit", "quit", "breakpoint")


def validate_expression(expr: str):
    expr = expr.strip()
    if not expr:
        return False, "Expression cannot be empty."
    if len(expr) > 256:
        return False, "Expression too long (max 256 chars)."
    low = expr.lower()
    for kw in DANGEROUS_KEYWORDS:
        if kw in low:
            return False, f"Forbidden keyword: '{kw}'"
    if not ALLOWED_EXPR_CHARS.match(expr):
        return False, "Expression contains invalid characters."
    if "var" not in expr:
        return False, "Expression must reference 'var'."
    try:
        compile(expr, "<expr>", "eval")
    except SyntaxError as e:
        return False, f"Syntax error: {e.msg}"
    try:
        result = eval(compile(expr, "<expr>", "eval"),
                      {"__builtins__": {}},
                      {"var": 0.5, "min": min, "max": max, "abs": abs, "round": round})
        if not isinstance(result, (int, float)):
            return False, "Expression must evaluate to a number."
    except Exception as ex:
        return False, f"Runtime error: {ex}"
    return True, ""


def validate_slider_range(low, high, label):
    if low >= high:
        return False, f"{label}: min ({low:.3f}) must be < max ({high:.3f})."
    if abs(high - low) < 0.001:
        return False, f"{label}: range too narrow."
    return True, ""


def validate_bone_collections(bone_colls):
    errors = []
    names_seen = set()
    for i, entry in enumerate(bone_colls):
        name = entry.coll_name.strip()
        terms_raw = entry.terms.strip()
        label = f"Collection [{i+1}]"

        if not name:
            errors.append(f"{label}: name cannot be empty.")
        elif name in names_seen:
            errors.append(f"{label}: duplicate name '{name}'.")
        else:
            names_seen.add(name)

        if not terms_raw:
            errors.append(f"'{name or label}': keywords cannot be empty.")
        else:
            terms = [t.strip() for t in terms_raw.split(",")]
            empty = [t for t in terms if not t]
            if empty:
                errors.append(f"'{name or label}': keywords contain empty entries (check commas).")

    return errors


def collect_all_errors(props, context):
    errors = []

    if props.armature_obj is None:
        errors.append("Armature not selected — use the eyedropper.")
    if props.face_mesh_obj is None:
        errors.append("Face Mesh not selected — use the eyedropper.")

    for label, lo, hi in [
        ("XRange L", props.xrange_l_min, props.xrange_l_max),
        ("XRange R", props.xrange_r_min, props.xrange_r_max),
        ("YRange L", props.yrange_l_min, props.yrange_l_max),
        ("YRange R", props.yrange_r_min, props.yrange_r_max),
    ]:
        ok, msg = validate_slider_range(lo, hi, label)
        if not ok:
            errors.append(msg)

    for label, expr in [
        ("XRange L", props.xrange_l_expr),
        ("XRange R", props.xrange_r_expr),
        ("YRange L", props.yrange_l_expr),
        ("YRange R", props.yrange_r_expr),
    ]:
        ok, msg = validate_expression(expr)
        if not ok:
            errors.append(f"{label} expression — {msg}")

    return errors


# ─────────────────────────────────────────────────────────────────────────────
#  PROPERTY GROUPS
# ─────────────────────────────────────────────────────────────────────────────

class UmaBoneCollEntry(PropertyGroup):
    """One bone collection: a name and a comma-separated list of keywords."""
    coll_name: StringProperty(
        name="Name",
        description="Bone collection name",
        default="New Collection",
    )
    terms: StringProperty(
        name="Keywords",
        description="Comma-separated match keywords (case-insensitive)",
        default="keyword",
    )


# Default collections seeded on first init
_DEFAULT_COLLECTIONS = [
    ("Hair",    "hair, ear, tail"),
    ("Cloth",   "shirt, jacket, skirt, ribbon, mantle, cloth, acc, sleeve"),
    ("Physics", "bust"),
    ("Face",    "cheek, nose"),
    ("Eyes",    "eye, eyebrow"),
    ("Mouth",   "mouth"),
]


class UmaEyeRigProps(PropertyGroup):

    # ── Object pickers (eyedropper) ───────────────────────────────────────────
    armature_obj: PointerProperty(
        name="Armature",
        description="Pick the rig armature object",
        type=bpy.types.Object,
        poll=_poll_armature,
    )
    face_mesh_obj: PointerProperty(
        name="Face Mesh",
        description="Pick the face mesh object (must have shape keys)",
        type=bpy.types.Object,
        poll=_poll_mesh,
    )

    # ── XRange L ──────────────────────────────────────────────────────────────
    xrange_l_min: FloatProperty(name="Min", default=-1.0,
        soft_min=-5.0, soft_max=0.0, step=10, precision=3,
        description="Shape key slider minimum for Eye_20 L (XRange)")
    xrange_l_max: FloatProperty(name="Max", default=1.4,
        soft_min=0.0, soft_max=5.0, step=10, precision=3,
        description="Shape key slider maximum for Eye_20 L (XRange)")
    xrange_l_expr: StringProperty(name="Expression", default="var * -1.5", maxlen=256,
        description="Driver expression — use 'var' for the rotation value")

    # ── XRange R ──────────────────────────────────────────────────────────────
    xrange_r_min: FloatProperty(name="Min", default=-0.4,
        soft_min=-5.0, soft_max=0.0, step=10, precision=3)
    xrange_r_max: FloatProperty(name="Max", default=1.4,
        soft_min=0.0, soft_max=5.0, step=10, precision=3)
    xrange_r_expr: StringProperty(name="Expression", default="var * -1.5", maxlen=256)

    # ── YRange L ──────────────────────────────────────────────────────────────
    yrange_l_min: FloatProperty(name="Min", default=-2.0,
        soft_min=-5.0, soft_max=0.0, step=10, precision=3)
    yrange_l_max: FloatProperty(name="Max", default=2.0,
        soft_min=0.0, soft_max=5.0, step=10, precision=3)
    yrange_l_expr: StringProperty(name="Expression", default="var * -1.5", maxlen=256)

    # ── YRange R ──────────────────────────────────────────────────────────────
    yrange_r_min: FloatProperty(name="Min", default=-2.0,
        soft_min=-5.0, soft_max=0.0, step=10, precision=3)
    yrange_r_max: FloatProperty(name="Max", default=2.0,
        soft_min=0.0, soft_max=5.0, step=10, precision=3)
    yrange_r_expr: StringProperty(name="Expression", default="var * 1.5", maxlen=256)

    # ── Bone collections ──────────────────────────────────────────────────────
    bone_collections: CollectionProperty(type=UmaBoneCollEntry)
    bone_coll_active: IntProperty(default=0)

    # ── UI state ──────────────────────────────────────────────────────────────
    show_xrange_l:  BoolProperty(default=True)
    show_xrange_r:  BoolProperty(default=True)
    show_yrange_l:  BoolProperty(default=True)
    show_yrange_r:  BoolProperty(default=True)
    show_advanced:  BoolProperty(default=False)
    show_bone_coll: BoolProperty(default=True)


# ─────────────────────────────────────────────────────────────────────────────
#  CORE RIG FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

EYE_CTRL_BONE         = "eye.ctrl"
EYE_CTRL_PARENT       = "head.x"
EYE_LOCATOR_L         = "Eye_locator_L"
EYE_LOCATOR_R         = "Eye_locator_R"
EYE_TARGET_LOCATOR_L  = "Eye_target_locator_L"
EYE_TARGET_LOCATOR_R  = "Eye_target_locator_R"

SK_XRANGE_L  = "Eye_20_L(XRange)[M_Face]"
SK_XRANGE_R  = "Eye_20_R(XRange)[M_Face]"
SK_YRANGE_L  = "Eye_21_L(YRange)[M_Face]"
SK_YRANGE_R  = "Eye_21_R(YRange)[M_Face]"
SK_CLOSE_L   = "Eye_2_L(CloseA)[M_Face]"
SK_CLOSE_R   = "Eye_2_R(CloseA)[M_Face]"
SK_ODOROKI_L = "Eye_12_L(OdorokiA)[M_Face]"
SK_ODOROKI_R = "Eye_12_R(OdorokiA)[M_Face]"

LIMIT_SCALE_MIN        = 0.8
LIMIT_SCALE_MAX        = 1.2
DAMPED_TRACK_AXIS      = 'TRACK_Z'
EYE_TARGET_SIDE_OFFSET = 0.03
EYE_CTRL_BONE_LENGTH   = 0.05


def _add_limit_scale(pose_bone):
    for c in list(pose_bone.constraints):
        if c.type == 'LIMIT_SCALE':
            pose_bone.constraints.remove(c)
    ls = pose_bone.constraints.new('LIMIT_SCALE')
    ls.name = "Limit Scale"
    for attr in ('min_x', 'min_y', 'min_z'):
        setattr(ls, 'use_' + attr, True); setattr(ls, attr, LIMIT_SCALE_MIN)
    for attr in ('max_x', 'max_y', 'max_z'):
        setattr(ls, 'use_' + attr, True); setattr(ls, attr, LIMIT_SCALE_MAX)
    ls.owner_space = 'LOCAL'


def _create_eye_ctrl_bone(armature_obj):
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode='EDIT')
    eb = armature_obj.data.edit_bones

    if EYE_CTRL_BONE in eb:
        eb.remove(eb[EYE_CTRL_BONE])

    loc_l = eb.get(EYE_LOCATOR_L)
    loc_r = eb.get(EYE_LOCATOR_R)
    if loc_l and loc_r:
        ctrl_head = (loc_l.head + loc_r.head) / 2 + mathutils.Vector((0, -0.15, 0))
    else:
        head_eb = eb.get(EYE_CTRL_PARENT)
        ctrl_head = (head_eb.head + mathutils.Vector((0, -0.15, 0.05))
                     if head_eb else mathutils.Vector((0, -0.15, 1.3)))

    new_bone = eb.new(EYE_CTRL_BONE)
    new_bone.head = ctrl_head
    new_bone.tail = ctrl_head + mathutils.Vector((0, 0, EYE_CTRL_BONE_LENGTH))
    new_bone.use_deform = False

    parent_eb = eb.get(EYE_CTRL_PARENT)
    if parent_eb:
        new_bone.parent = parent_eb
        new_bone.use_connect = False

    bpy.ops.object.mode_set(mode='POSE')
    pb = armature_obj.pose.bones.get(EYE_CTRL_BONE)
    if pb is None:
        raise RuntimeError("eye.ctrl pose bone not accessible after creation.")
    _add_limit_scale(pb)


def _reposition_eye_target_locators(armature_obj):
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode='EDIT')
    eb = armature_obj.data.edit_bones

    ctrl_eb = eb.get(EYE_CTRL_BONE)
    if ctrl_eb is None:
        bpy.ops.object.mode_set(mode='POSE')
        raise RuntimeError("eye.ctrl not found for target locator repositioning.")

    ctrl_pos = ctrl_eb.head.copy()
    for bone_name, side_x in [(EYE_TARGET_LOCATOR_L,  EYE_TARGET_SIDE_OFFSET),
                               (EYE_TARGET_LOCATOR_R, -EYE_TARGET_SIDE_OFFSET)]:
        bone = eb.get(bone_name)
        if bone is None:
            continue
        new_head = ctrl_pos + mathutils.Vector((side_x, 0, 0))
        bone.head = new_head
        bone.tail = new_head + mathutils.Vector((0, 0, EYE_CTRL_BONE_LENGTH))
        bone.parent = ctrl_eb
        bone.use_connect = False

    bpy.ops.object.mode_set(mode='POSE')


def _setup_eye_locator(armature_obj, locator_bone, target_locator_bone):
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode='POSE')

    pb = armature_obj.pose.bones.get(locator_bone)
    if pb is None:
        bpy.ops.object.mode_set(mode='OBJECT')
        return

    for c in list(pb.constraints):
        if c.type in ('DAMPED_TRACK', 'COPY_SCALE', 'LIMIT_SCALE'):
            pb.constraints.remove(c)

    dt = pb.constraints.new('DAMPED_TRACK')
    dt.name, dt.target, dt.subtarget, dt.track_axis = "Damped Track", armature_obj, target_locator_bone, DAMPED_TRACK_AXIS

    cs = pb.constraints.new('COPY_SCALE')
    cs.name, cs.target, cs.subtarget = "Copy Scale", armature_obj, EYE_CTRL_BONE
    cs.use_x = cs.use_y = cs.use_z = True
    cs.use_offset = False
    cs.target_space = cs.owner_space = 'LOCAL'

    _add_limit_scale(pb)
    bpy.ops.object.mode_set(mode='POSE')


def _remove_driver(shape_keys, sk_name):
    if not shape_keys.animation_data:
        return
    fc = shape_keys.animation_data.drivers.find(f'key_blocks["{sk_name}"].value')
    if fc:
        shape_keys.animation_data.drivers.remove(fc)


def _setup_rotation_driver(face_mesh_obj, armature_obj, sk_name, bone_name,
                             rot_axis_index, expression, slider_min, slider_max):
    sk = face_mesh_obj.data.shape_keys
    if not sk or sk_name not in sk.key_blocks:
        print(f"[EyeSetup] WARNING: Shape key '{sk_name}' not found — skipping.")
        return
    sk.animation_data_create()
    _remove_driver(sk, sk_name)

    kb = sk.key_blocks[sk_name]
    kb.slider_min, kb.slider_max = slider_min, slider_max

    driver = kb.driver_add("value").driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.name, var.type = "var", 'TRANSFORMS'
    t = var.targets[0]
    t.id, t.bone_target = armature_obj, bone_name
    t.transform_type = ['ROT_X', 'ROT_Y', 'ROT_Z'][rot_axis_index]
    t.transform_space, t.rotation_mode = 'LOCAL_SPACE', 'AUTO'
    driver.expression = expression


def _setup_scale_driver(face_mesh_obj, armature_obj, sk_name, locator_bone, expression):
    sk = face_mesh_obj.data.shape_keys
    if not sk or sk_name not in sk.key_blocks:
        print(f"[EyeSetup] WARNING: Shape key '{sk_name}' not found — skipping.")
        return
    sk.animation_data_create()
    _remove_driver(sk, sk_name)

    driver = sk.key_blocks[sk_name].driver_add("value").driver
    driver.type = 'SCRIPTED'
    var = driver.variables.new()
    var.name, var.type = "var", 'TRANSFORMS'
    t = var.targets[0]
    t.id, t.bone_target = armature_obj, locator_bone
    t.transform_type, t.transform_space = 'SCALE_AVG', 'LOCAL_SPACE'
    driver.expression = expression


def _setup_bone_collections(armature_obj, bone_coll_prop):
    """Build collections from the panel's CollectionProperty."""
    arm = armature_obj.data
    collections = arm.collections

    # Build dict from panel props
    coll_dict = {}
    for entry in bone_coll_prop:
        name = entry.coll_name.strip()
        terms = [t.strip().lower() for t in entry.terms.split(",") if t.strip()]
        if name and terms:
            coll_dict[name] = terms

    # Remove & recreate
    coll_map = {}
    for name in coll_dict:
        if name in collections:
            collections.remove(collections[name])
        coll_map[name] = collections.new(name)

    # Assign bones — first matching collection wins; unmatched stay unassigned
    counts = {name: 0 for name in coll_dict}
    for bone in arm.bones:
        bone_name_lower = bone.name.lower()
        for coll_name, terms in coll_dict.items():
            if any(term in bone_name_lower for term in terms):
                coll_map[coll_name].assign(bone)
                counts[coll_name] += 1
                break  # stop at first match so bone isn't in multiple collections

    return counts


# ─────────────────────────────────────────────────────────────────────────────
#  BONE COLLECTION OPERATORS
# ─────────────────────────────────────────────────────────────────────────────

class UMAEYERIG_OT_coll_add(Operator):
    """Add a new bone collection entry"""
    bl_idname  = "uma_eye_rig.coll_add"
    bl_label   = "Add Collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.uma_eye_rig
        entry = props.bone_collections.add()
        entry.coll_name = "New Collection"
        entry.terms = "keyword"
        props.bone_coll_active = len(props.bone_collections) - 1
        return {'FINISHED'}


class UMAEYERIG_OT_coll_remove(Operator):
    """Remove the selected bone collection entry"""
    bl_idname  = "uma_eye_rig.coll_remove"
    bl_label   = "Remove Collection"
    bl_options = {'REGISTER', 'UNDO'}

    index: IntProperty()

    def execute(self, context):
        props = context.scene.uma_eye_rig
        if 0 <= self.index < len(props.bone_collections):
            props.bone_collections.remove(self.index)
            props.bone_coll_active = max(0, self.index - 1)
        return {'FINISHED'}


class UMAEYERIG_OT_coll_move(Operator):
    """Move a bone collection entry up or down"""
    bl_idname  = "uma_eye_rig.coll_move"
    bl_label   = "Move Collection"
    bl_options = {'REGISTER', 'UNDO'}

    index:     IntProperty()
    direction: IntProperty()  # -1 = up, +1 = down

    def execute(self, context):
        props = context.scene.uma_eye_rig
        col = props.bone_collections
        target = self.index + self.direction
        if 0 <= target < len(col):
            col.move(self.index, target)
            props.bone_coll_active = target
        return {'FINISHED'}


class UMAEYERIG_OT_coll_reset(Operator):
    """Reset bone collections to the script defaults"""
    bl_idname  = "uma_eye_rig.coll_reset"
    bl_label   = "Reset to Defaults"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.uma_eye_rig
        props.bone_collections.clear()
        for name, terms in _DEFAULT_COLLECTIONS:
            e = props.bone_collections.add()
            e.coll_name = name
            e.terms = terms
        self.report({'INFO'}, "Bone collections reset to defaults.")
        return {'FINISHED'}


# ─────────────────────────────────────────────────────────────────────────────
#  MAIN OPERATORS
# ─────────────────────────────────────────────────────────────────────────────

class UMAEYERIG_OT_validate(Operator):
    """Validate all settings without running the setup"""
    bl_idname  = "uma_eye_rig.validate"
    bl_label   = "Validate Settings"
    bl_options = {'REGISTER'}

    def execute(self, context):
        props  = context.scene.uma_eye_rig
        errors = collect_all_errors(props, context)
        if errors:
            for e in errors:
                self.report({'ERROR'}, e)
            self.report({'WARNING'}, f"{len(errors)} error(s) — see Info header.")
        else:
            self.report({'INFO'}, "All settings valid ✓")
        return {'FINISHED'}


class UMAEYERIG_OT_run(Operator):
    """Run the full UmaMusume Eye Rig setup"""
    bl_idname  = "uma_eye_rig.run"
    bl_label   = "Build Eye Rig"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props  = context.scene.uma_eye_rig
        errors = collect_all_errors(props, context)

        if errors:
            for e in errors:
                self.report({'ERROR'}, e)
            return {'CANCELLED'}

        armature_obj = props.armature_obj
        face_mesh    = props.face_mesh_obj

        try:
            _create_eye_ctrl_bone(armature_obj)
            _reposition_eye_target_locators(armature_obj)
            _setup_eye_locator(armature_obj, EYE_LOCATOR_L, EYE_TARGET_LOCATOR_L)
            _setup_eye_locator(armature_obj, EYE_LOCATOR_R, EYE_TARGET_LOCATOR_R)

            _setup_rotation_driver(face_mesh, armature_obj, SK_XRANGE_L, EYE_LOCATOR_L, 1,
                                   props.xrange_l_expr, props.xrange_l_min, props.xrange_l_max)
            _setup_rotation_driver(face_mesh, armature_obj, SK_XRANGE_R, EYE_LOCATOR_R, 1,
                                   props.xrange_r_expr, props.xrange_r_min, props.xrange_r_max)
            _setup_rotation_driver(face_mesh, armature_obj, SK_YRANGE_L, EYE_LOCATOR_L, 0,
                                   props.yrange_l_expr, props.yrange_l_min, props.yrange_l_max)
            _setup_rotation_driver(face_mesh, armature_obj, SK_YRANGE_R, EYE_LOCATOR_R, 0,
                                   props.yrange_r_expr, props.yrange_r_min, props.yrange_r_max)

            close_expr   = "min(max((1 - var) / (1 - 0.8), 0.0), 1.0)"
            odoroki_expr = "min(max((var - 1) / (1.2 - 1), 0.0), 1.0)"
            for sk, bone in [(SK_CLOSE_L, EYE_LOCATOR_L), (SK_CLOSE_R, EYE_LOCATOR_R)]:
                _setup_scale_driver(face_mesh, armature_obj, sk, bone, close_expr)
            for sk, bone in [(SK_ODOROKI_L, EYE_LOCATOR_L), (SK_ODOROKI_R, EYE_LOCATOR_R)]:
                _setup_scale_driver(face_mesh, armature_obj, sk, bone, odoroki_expr)

            counts = _setup_bone_collections(armature_obj, props.bone_collections)
            bpy.context.view_layer.update()

        except Exception as ex:
            try:
                bpy.ops.object.mode_set(mode='POSE')
            except Exception:
                pass
            self.report({'ERROR'}, f"Setup failed: {ex}")
            return {'CANCELLED'}

        coll_summary = "  |  ".join(f"{k}: {v}" for k, v in counts.items())
        self.report({'INFO'}, f"Done!  {coll_summary}")
        return {'FINISHED'}


class UMAEYERIG_OT_reset_drivers(Operator):
    """Reset driver sliders and expressions to script defaults"""
    bl_idname  = "uma_eye_rig.reset_drivers"
    bl_label   = "Reset Drivers to Defaults"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        p = context.scene.uma_eye_rig
        p.xrange_l_min = -1.0;  p.xrange_l_max = 1.4;  p.xrange_l_expr = "var * -1.5"
        p.xrange_r_min = -0.4;  p.xrange_r_max = 1.4;  p.xrange_r_expr = "var * -1.5"
        p.yrange_l_min = -2.0;  p.yrange_l_max = 2.0;  p.yrange_l_expr = "var * -1.5"
        p.yrange_r_min = -2.0;  p.yrange_r_max = 2.0;  p.yrange_r_expr = "var * 1.5"
        self.report({'INFO'}, "Driver defaults restored.")
        return {'FINISHED'}


# ─────────────────────────────────────────────────────────────────────────────
#  PANEL DRAW HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def _draw_shape_key_block(layout, props, label, icon,
                           show_attr, min_attr, max_attr, expr_attr):
    box  = layout.box()
    row  = box.row()
    show = getattr(props, show_attr)
    row.prop(props, show_attr,
             icon='TRIA_DOWN' if show else 'TRIA_RIGHT',
             icon_only=True, emboss=False)
    row.label(text=label, icon=icon)

    if not show:
        return

    col = box.column(align=True)
    col.label(text="Shape Key Slider Range:", icon='ARROW_LEFTRIGHT')
    row2 = col.row(align=True)
    row2.prop(props, min_attr, text="Min")
    row2.prop(props, max_attr, text="Max")

    if getattr(props, min_attr) >= getattr(props, max_attr):
        r = box.row(); r.alert = True
        r.label(text="⚠  Min must be less than Max", icon='ERROR')

    box.separator(factor=0.4)
    col2 = box.column(align=True)
    col2.label(text="Driver Expression  (use 'var'):", icon='DRIVER')
    col2.prop(props, expr_attr, text="")

    ok, msg = validate_expression(getattr(props, expr_attr))
    if not ok:
        r = box.row(); r.alert = True
        r.label(text=f"⚠  {msg}", icon='ERROR')
    else:
        r = box.row(); r.enabled = False
        r.label(text="✓ Expression OK", icon='CHECKMARK')


def _draw_bone_collections(layout, props):
    """Editable bone collections section."""
    outer = layout.box()
    hrow  = outer.row()
    hrow.prop(props, "show_bone_coll",
              icon='TRIA_DOWN' if props.show_bone_coll else 'TRIA_RIGHT',
              icon_only=True, emboss=False)
    hrow.label(text="Bone Collections", icon='GROUP_BONE')

    # Add / Reset buttons always visible in header
    hrow.operator("uma_eye_rig.coll_add",   text="", icon='ADD')
    hrow.operator("uma_eye_rig.coll_reset",  text="", icon='LOOP_BACK')

    if not props.show_bone_coll:
        return

    if len(props.bone_collections) == 0:
        r = outer.row(); r.alert = True
        r.label(text="No collections defined. Click + to add.", icon='INFO')
        return

    for i, entry in enumerate(props.bone_collections):
        box = outer.box()

        # ── Header row: name + move/remove buttons ────────────────────────
        hdr = box.row(align=True)
        hdr.prop(entry, "coll_name", text="", icon='GROUP_BONE')

        sub = hdr.row(align=True)
        sub.scale_x = 0.75
        op_up = sub.operator("uma_eye_rig.coll_move", text="", icon='TRIA_UP')
        op_up.index, op_up.direction = i, -1
        op_dn = sub.operator("uma_eye_rig.coll_move", text="", icon='TRIA_DOWN')
        op_dn.index, op_dn.direction = i, 1
        op_rm = sub.operator("uma_eye_rig.coll_remove", text="", icon='X')
        op_rm.index = i

        # ── Keywords field (always visible) ───────────────────────────────
        kw_col = box.column(align=True)
        kw_col.label(text="Keywords (comma-separated):", icon='FONTPREVIEW')
        kw_col.prop(entry, "terms", text="")

        # Per-entry validation feedback
        name = entry.coll_name.strip()
        terms_raw = entry.terms.strip()
        row_ok = True

        if not name:
            r = box.row(); r.alert = True
            r.label(text="⚠  Name cannot be empty", icon='ERROR')
            row_ok = False

        if not terms_raw:
            r = box.row(); r.alert = True
            r.label(text="⚠  Keywords cannot be empty", icon='ERROR')
            row_ok = False
        else:
            terms = [t.strip() for t in terms_raw.split(",")]
            empty = [t for t in terms if not t]
            if empty:
                r = box.row(); r.alert = True
                r.label(text="⚠  Empty keyword (double comma?)", icon='ERROR')
                row_ok = False

        if row_ok:
            parsed = [t.strip() for t in terms_raw.split(",") if t.strip()]
            r = box.row(); r.enabled = False
            r.label(text=f"✓  {len(parsed)} keyword(s)", icon='CHECKMARK')


# ─────────────────────────────────────────────────────────────────────────────
#  MAIN PANEL
# ─────────────────────────────────────────────────────────────────────────────

class UMAEYERIG_PT_main(Panel):
    bl_label       = "Uma Eye Rig"
    bl_idname      = "UMAEYERIG_PT_main"
    bl_space_type  = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category    = "Uma Eye Rig"

    def draw(self, context):
        layout = self.layout
        props  = context.scene.uma_eye_rig

        # ── Object pickers ────────────────────────────────────────────────
        obj_box = layout.box()
        obj_box.label(text="Scene Objects", icon='SCENE_DATA')

        row = obj_box.row(align=True)
        row.alert = props.armature_obj is None
        row.prop(props, "armature_obj", text="Armature", icon='ARMATURE_DATA')

        row2 = obj_box.row(align=True)
        row2.alert = props.face_mesh_obj is None
        row2.prop(props, "face_mesh_obj", text="Face Mesh", icon='MESH_DATA')

        layout.separator(factor=0.6)

        # ── Shape key drivers ─────────────────────────────────────────────
        layout.label(text="Shape Key Drivers", icon='SHAPEKEY_DATA')

        _draw_shape_key_block(layout, props,
            "Eye_20_L  XRange  (Horizontal Left)",  'EVENT_L',
            'show_xrange_l', 'xrange_l_min', 'xrange_l_max', 'xrange_l_expr')
        _draw_shape_key_block(layout, props,
            "Eye_20_R  XRange  (Horizontal Right)", 'EVENT_R',
            'show_xrange_r', 'xrange_r_min', 'xrange_r_max', 'xrange_r_expr')
        _draw_shape_key_block(layout, props,
            "Eye_21_L  YRange  (Vertical Left)",    'EVENT_L',
            'show_yrange_l', 'yrange_l_min', 'yrange_l_max', 'yrange_l_expr')
        _draw_shape_key_block(layout, props,
            "Eye_21_R  YRange  (Vertical Right)",   'EVENT_R',
            'show_yrange_r', 'yrange_r_min', 'yrange_r_max', 'yrange_r_expr')

        # ── Fixed scale drivers (info) ────────────────────────────────────
        adv = layout.box()
        adv.prop(props, "show_advanced",
                 icon='TRIA_DOWN' if props.show_advanced else 'TRIA_RIGHT',
                 text="Scale Drivers (fixed expressions)", emboss=False)
        if props.show_advanced:
            col = adv.column(align=True); col.enabled = False; col.scale_y = 0.8
            col.label(text="CloseA   ← min(max((1-var)/(1-0.8), 0), 1)",   icon='RESTRICT_INSTANCED_OFF')
            col.label(text="OdorokiA ← min(max((var-1)/(1.2-1), 0), 1)",   icon='RESTRICT_INSTANCED_OFF')

        layout.separator(factor=0.4)

        # Driver reset button
        layout.operator("uma_eye_rig.reset_drivers", text="Reset Driver Defaults", icon='LOOP_BACK')

        layout.separator(factor=0.6)

        # ── Bone collections ──────────────────────────────────────────────
        _draw_bone_collections(layout, props)

        layout.separator(factor=0.8)

        # ── Action buttons ────────────────────────────────────────────────
        errors = collect_all_errors(props, context)

        row_btns = layout.row(align=True)
        row_btns.scale_y = 1.2
        row_btns.operator("uma_eye_rig.validate", icon='CHECKMARK', text="Validate All")

        layout.separator(factor=0.3)

        run_row = layout.row()
        run_row.scale_y = 1.8
        run_row.enabled = not bool(errors)
        run_row.operator("uma_eye_rig.run", icon='PLAY', text="Build Eye Rig")

        if errors:
            layout.separator(factor=0.3)
            err_box = layout.box()
            err_box.alert = True
            err_box.label(text=f"Fix {len(errors)} error(s) to enable build:", icon='ERROR')
            for e in errors[:5]:
                r = err_box.row(); r.scale_y = 0.75
                r.label(text=f"• {e}")
            if len(errors) > 5:
                err_box.label(text=f"  … and {len(errors)-5} more (Validate for full list)")


# ─────────────────────────────────────────────────────────────────────────────
#  REGISTRATION
# ─────────────────────────────────────────────────────────────────────────────

_classes = (
    UmaBoneCollEntry,
    UmaEyeRigProps,
    UMAEYERIG_OT_coll_add,
    UMAEYERIG_OT_coll_remove,
    UMAEYERIG_OT_coll_move,
    UMAEYERIG_OT_coll_reset,
    UMAEYERIG_OT_validate,
    UMAEYERIG_OT_run,
    UMAEYERIG_OT_reset_drivers,
    UMAEYERIG_PT_main,
)


def _seed_bone_collections(dummy=None):
    """Called on depsgraph post-update to seed defaults once."""
    for scene in bpy.data.scenes:
        props = scene.uma_eye_rig
        if len(props.bone_collections) == 0:
            for name, terms in _DEFAULT_COLLECTIONS:
                e = props.bone_collections.add()
                e.coll_name = name
                e.terms = terms
        # Remove handler after first run
    if _seed_bone_collections in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(_seed_bone_collections)


def register():
    for cls in _classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.uma_eye_rig = PointerProperty(type=UmaEyeRigProps)
    # Seed defaults on first depsgraph update (scene may not exist at register time)
    bpy.app.handlers.depsgraph_update_post.append(_seed_bone_collections)


def unregister():
    if _seed_bone_collections in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(_seed_bone_collections)
    for cls in reversed(_classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.uma_eye_rig


if __name__ == "__main__":
    register()