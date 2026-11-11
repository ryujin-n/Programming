bl_info = {
    "name": "Shape Key Face Control Panel",
    "author": "ryujin",
    "version": (2, 2, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar (N) > Shape Keys",
    "description": "Shape key controller bc im lazy to do it myself ?:p",
    "category": "Object",
}

import bpy
import re
import numpy as np
from bpy.props import (
    PointerProperty, StringProperty, BoolProperty, IntProperty, EnumProperty,
    CollectionProperty,
)
from bpy.types import PropertyGroup, Panel, Operator, UIList

CATEGORY_KEYWORDS = [
    ("Eyebrow", {"eyebrow", "eyebrows", "brow", "brows"}),
    ("Eyes",    {"eyes", "eye"}),
    ("Mouth",   {"mouth", "lip", "lips"}),
    ("Ear",     {"ear", "ears"}),
]

SEPARATOR_NAME = "==== both ===="

CATEGORY_ORDER = ["Eyes", "Eyebrow", "Mouth", "Ear", "Other"]

CATEGORY_LABELS = {
    "Eyes": "Eyes",
    "Eyebrow": "Eyebrows",
    "Mouth": "Mouth",
    "Ear": "Ears",
    "Other": "Other",
}

CATEGORY_ICONS = {
    "Eyes": "HIDE_OFF",
    "Eyebrow": "MOD_HUE_SATURATION",
    "Mouth": "MESH_CIRCLE",
    "Ear": "SPEAKER",
    "Other": "SHAPEKEY_DATA",
}


def has_lr_specifier(name):
    """Detecta se o nome tem um token isolado 'L' ou 'R' (ex: _R, _L),
    mesmo que venha seguido de outros sufixos como (WaraiA)[M_Face]."""
    tokens = [t.lower() for t in re.split(r'[^a-zA-Z0-9]+', name) if t]
    return 'l' in tokens or 'r' in tokens


def get_category(name):
    """Retorna a categoria (feature) de uma shape key com base no nome,
    independente de ser Single ou Both."""
    tokens = [t for t in re.split(r'[^a-zA-Z]+', name.lower()) if t]
    token_set = set(tokens)

    for cat, keywords in CATEGORY_KEYWORDS:
        if keywords & token_set:
            return cat

    # fallback por substring, caso o nome nao esteja separado por "_"
    lower_name = name.lower()
    for cat, keywords in CATEGORY_KEYWORDS:
        if any(kw in lower_name for kw in keywords):
            return cat

    return "Other"


def is_valid_target(obj):
    return (
        obj is not None
        and obj.type == 'MESH'
        and obj.data is not None
        and obj.data.shape_keys is not None
        and len(obj.data.shape_keys.key_blocks) > 1
    )


def target_poll(self, obj):
    return is_valid_target(obj)


def compute_grouped(obj, single):
    """Agrupa as shape keys por categoria (feature), filtrando apenas as
    que tem (single=True) ou nao tem (single=False) especificador L/R."""
    keys = [k for k in obj.data.shape_keys.key_blocks
            if k.name != "Basis" and k.name != SEPARATOR_NAME]
    grouped = {c: [] for c in CATEGORY_ORDER}
    for k in keys:
        if has_lr_specifier(k.name) != single:
            continue
        grouped[get_category(k.name)].append(k.name)
    return grouped


# ---------------------------------------------------------------------------
# Utilitarios de animacao / keyframe
# ---------------------------------------------------------------------------

def kf_data_path(key_name):
    return 'key_blocks["%s"].value' % key_name


def get_fcurve(shape_keys, key_name):
    """Retorna o FCurve do valor de uma shape key, se existir."""
    anim = shape_keys.animation_data
    if not anim or not anim.action:
        return None
    return anim.action.fcurves.find(kf_data_path(key_name))


def has_keyframe_at(fcurve, frame):
    if fcurve is None:
        return False
    for kp in fcurve.keyframe_points:
        if round(kp.co.x) == frame:
            return True
    return False


def is_animated(fcurve):
    return fcurve is not None and len(fcurve.keyframe_points) > 0


# ---------------------------------------------------------------------------
# Sincronizacao das listas (UIList precisa de CollectionProperty "de verdade")
# ---------------------------------------------------------------------------

def sync_shapekey_list(settings, obj):
    """Preenche a lista (nivel 2) de shape keys da categoria selecionada."""
    settings.category_keys.clear()
    if not is_valid_target(obj):
        return
    if not (0 <= settings.categories_index < len(settings.categories)):
        return

    cat_key = settings.categories[settings.categories_index].key
    single = settings.variant == 'SINGLE'
    grouped = compute_grouped(obj, single)
    names = grouped.get(cat_key, [])

    if settings.search_filter:
        f = settings.search_filter.lower()
        names = [n for n in names if f in n.lower()]

    prev_selected = None
    if 0 <= settings.category_keys_index < len(settings.category_keys):
        prev_selected = settings.category_keys[settings.category_keys_index].name

    new_index = 0
    for n in names:
        item = settings.category_keys.add()
        item.name = n
        if n == prev_selected:
            new_index = len(settings.category_keys) - 1

    settings.category_keys_index = min(new_index, max(0, len(settings.category_keys) - 1))


def _on_categories_index_update(self, context):
    sync_shapekey_list(self, self.target_object)


def _on_search_filter_update(self, context):
    sync_shapekey_list(self, self.target_object)


def _on_variant_update(self, context):
    self["_cat_sig"] = ""  # forca resync (Single e Both usam listas diferentes)
    sync_category_list(self, self.target_object)


def sync_category_list(settings, obj):
    """Preenche a lista (nivel 1) de categorias para a aba (Single/Both) atual.
    So reconstroi quando os nomes das shape keys ou a aba realmente mudam,
    para nao perder a selecao atual a cada redraw do painel."""
    if not is_valid_target(obj):
        settings.categories.clear()
        settings.category_keys.clear()
        settings["_cat_sig"] = ""  # listas vazias -> invalida o cache
        return

    single = settings.variant == 'SINGLE'
    grouped = compute_grouped(obj, single)
    has_any = any(grouped[c] for c in CATEGORY_ORDER)
    signature = obj.name + "||" + settings.variant + "||" + "|".join(
        "%s:%s" % (c, ",".join(grouped[c])) for c in CATEGORY_ORDER
    )
    # so pula o rebuild se o cache bate E as listas realmente estao populadas
    if settings.get("_cat_sig") == signature and (len(settings.categories) > 0 or not has_any):
        return
    settings["_cat_sig"] = signature

    prev_selected = None
    if 0 <= settings.categories_index < len(settings.categories):
        prev_selected = settings.categories[settings.categories_index].key

    settings.categories.clear()
    new_index = 0
    for cat in CATEGORY_ORDER:
        names = grouped[cat]
        if not names:
            continue
        item = settings.categories.add()
        item.key = cat
        item.label = CATEGORY_LABELS[cat]
        item.icon = CATEGORY_ICONS.get(cat, 'SHAPEKEY_DATA')
        if cat == prev_selected:
            new_index = len(settings.categories) - 1

    settings.categories_index = min(new_index, max(0, len(settings.categories) - 1))
    sync_shapekey_list(settings, obj)


# ---------------------------------------------------------------------------
# Combiner (junta _L + _R em uma shape key "Both")
# ---------------------------------------------------------------------------

def _base_name(name, side):
    tag = '_' + side
    if name.endswith(tag):
        return name.replace(tag + '(', '(').replace(tag + '[', '[').replace(tag, '', 1)
    return name.replace(tag + '(', '(').replace(tag + '[', '[')


def combine_lr_shapekeys(obj):
    """Cria as shape keys combinadas (L + R) que ainda nao existem.
    Idempotente: pode rodar quantas vezes quiser. Retorna quantas criou."""
    if not is_valid_target(obj):
        return 0

    key_blocks = obj.data.shape_keys.key_blocks
    pairs = {}  # base_name -> {'L': nome, 'R': nome}

    for sk in key_blocks:
        name = sk.name
        low = name.lower()
        if name == SEPARATOR_NAME or 'xrange' in low or 'yrange' in low:
            continue
        for side in ('R', 'L'):
            tag = '_' + side
            if tag + '(' in name or tag + '[' in name or name.endswith(tag):
                pairs.setdefault(_base_name(name, side), {})[side] = name
                break

    todo = [b for b, p in pairs.items()
            if 'L' in p and 'R' in p and b not in key_blocks]
    if not todo:
        return 0

    if SEPARATOR_NAME not in key_blocks:
        obj.shape_key_add(name=SEPARATOR_NAME, from_mix=False)
        sep = obj.data.shape_keys.key_blocks[SEPARATOR_NAME]
        sep.value = 0.0
        sep.mute = True
        sep.lock_shape = True
        sep.slider_min = 0.0
        sep.slider_max = 0.0

    # as referencias a key_blocks podem ficar invalidas ao adicionar keys,
    # entao tudo e re-buscado pelo nome a cada iteracao
    def read_co(name):
        kb = obj.data.shape_keys.key_blocks[name]
        arr = np.empty(len(kb.data) * 3, dtype=np.float32)
        kb.data.foreach_get("co", arr)
        return arr

    basis_name = obj.data.shape_keys.key_blocks[0].name
    created = 0
    for base_name in todo:
        co_basis = read_co(basis_name)
        co_l = read_co(pairs[base_name]['L'])
        co_r = read_co(pairs[base_name]['R'])

        obj.shape_key_add(name=base_name, from_mix=False)
        new_sk = obj.data.shape_keys.key_blocks[base_name]
        new_sk.value = 0.0
        new_sk.data.foreach_set("co", co_basis + (co_l - co_basis) + (co_r - co_basis))
        created += 1

    return created


def prepare_target(settings, obj):
    """Roda o combiner PRIMEIRO e so depois monta as listas do controlador."""
    if is_valid_target(obj):
        try:
            combine_lr_shapekeys(obj)
        except Exception as e:
            print("[SMK] combiner falhou:", e)
    settings["_cat_sig"] = ""  # forca resync
    sync_category_list(settings, obj)


def _on_target_object_update(self, context):
    prepare_target(self, self.target_object)


# ---------------------------------------------------------------------------
# Property Groups
# ---------------------------------------------------------------------------

class SMK_CategoryItem(PropertyGroup):
    key: StringProperty()
    label: StringProperty()
    icon: StringProperty()


class SMK_ShapeKeyRef(PropertyGroup):
    name: StringProperty()


class SMK_PropertyGroup(PropertyGroup):
    target_object: PointerProperty(
        name="Object",
        type=bpy.types.Object,
        poll=target_poll,
        description="Shape key's Mesh",
        update=_on_target_object_update,
    )
    variant: EnumProperty(
        name="Variant",
        items=[
            ('SINGLE', "Single", "Shape keys com lado especifico (_L / _R)"),
            ('BOTH', "Both", "Shape keys simetricas (sem especificador L/R)"),
        ],
        default='SINGLE',
        update=_on_variant_update,
    )
    search_filter: StringProperty(
        name="Search",
        default="",
        description="Shape key's name filter",
        update=_on_search_filter_update,
    )
    categories: CollectionProperty(type=SMK_CategoryItem)
    categories_index: IntProperty(default=0, update=_on_categories_index_update)
    category_keys: CollectionProperty(type=SMK_ShapeKeyRef)
    category_keys_index: IntProperty(default=0)


# ---------------------------------------------------------------------------
# UILists
# ---------------------------------------------------------------------------

class SMK_UL_categories(UIList):
    bl_idname = "SMK_UL_categories"

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        row = layout.row(align=True)
        row.label(text="", icon=item.icon if item.icon else 'SHAPEKEY_DATA')
        row.label(text=item.label)
        op = row.operator("smk.reset_category", text="", icon="LOOP_BACK", emboss=False)
        op.category = item.key
        op.single = (data.variant == 'SINGLE')


class SMK_UL_shapekeys(UIList):
    bl_idname = "SMK_UL_shapekeys"

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        obj = data.target_object
        row = layout.row(align=True)

        key = None
        fcurve = None
        if is_valid_target(obj):
            key = obj.data.shape_keys.key_blocks.get(item.name)
            fcurve = get_fcurve(obj.data.shape_keys, item.name)
        anim_icon = 'KEY_HLT' if is_animated(fcurve) else 'SHAPEKEY_DATA'

        row.label(text="", icon=anim_icon)

        if key is not None:
            row.prop(key, "value", text=item.name, slider=True)
        else:
            row.label(text=item.name)

        op = row.operator("smk.reset_key", text="", icon="LOOP_BACK", emboss=False)
        op.key_name = item.name


# ---------------------------------------------------------------------------
# Operators
# ---------------------------------------------------------------------------

class SMK_OT_use_active(Operator):
    bl_idname = "smk.use_active_object"
    bl_label = "Use active object"
    bl_description = "Defines target active object"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return is_valid_target(context.active_object)

    def execute(self, context):
        settings = context.scene.shapekey_manager
        settings.target_object = context.active_object
        prepare_target(settings, settings.target_object)
        self.report({'INFO'}, "Alvo definido: %s" % context.active_object.name)
        return {'FINISHED'}


class SMK_OT_refresh(Operator):
    bl_idname = "smk.refresh"
    bl_label = "Refresh"
    bl_description = "Re-runs the L+R combiner and rebuilds the lists for the target mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        settings = context.scene.shapekey_manager
        obj = settings.target_object
        if not is_valid_target(obj):
            self.report({'ERROR'}, "Nenhum objeto alvo valido")
            return {'CANCELLED'}
        prepare_target(settings, obj)
        return {'FINISHED'}


class SMK_OT_reset_key(Operator):
    bl_idname = "smk.reset_key"
    bl_label = "Reset"
    bl_description = "Resets this shape key's value to 0.0"
    bl_options = {'REGISTER', 'UNDO'}

    key_name: StringProperty()

    def execute(self, context):
        settings = context.scene.shapekey_manager
        obj = settings.target_object
        if not is_valid_target(obj):
            self.report({'ERROR'}, "Nenhum objeto alvo valido")
            return {'CANCELLED'}
        key = obj.data.shape_keys.key_blocks.get(self.key_name)
        if key:
            key.value = 0.0
        return {'FINISHED'}


class SMK_OT_reset_category(Operator):
    bl_idname = "smk.reset_category"
    bl_label = "Reset Category"
    bl_description = "Resets every shape key in this category (current tab) to 0.0"
    bl_options = {'REGISTER', 'UNDO'}

    category: StringProperty()
    single: BoolProperty(default=True)

    def execute(self, context):
        settings = context.scene.shapekey_manager
        obj = settings.target_object
        if not is_valid_target(obj) or not self.category:
            self.report({'ERROR'}, "Nenhuma categoria valida")
            return {'CANCELLED'}
        count = 0
        for key in obj.data.shape_keys.key_blocks:
            if key.name == "Basis":
                continue
            if get_category(key.name) == self.category and has_lr_specifier(key.name) == self.single:
                key.value = 0.0
                count += 1
        self.report({'INFO'}, "%d shape keys reset: %s" % (count, self.category))
        return {'FINISHED'}


class SMK_OT_toggle_keyframe(Operator):
    bl_idname = "smk.toggle_keyframe"
    bl_label = "Insert/Remove Keyframe"
    bl_description = "Insert a keyframe for this shape key value at the current frame.\nCtrl+Click to remove the keyframe at the current frame"
    bl_options = {'REGISTER', 'UNDO'}

    key_name: StringProperty()

    def invoke(self, context, event):
        self._remove = event.ctrl
        return self.execute(context)

    def execute(self, context):
        settings = context.scene.shapekey_manager
        obj = settings.target_object
        if not is_valid_target(obj):
            self.report({'ERROR'}, "Nenhum objeto alvo valido")
            return {'CANCELLED'}

        shape_keys = obj.data.shape_keys
        key = shape_keys.key_blocks.get(self.key_name)
        if key is None:
            return {'CANCELLED'}

        frame = context.scene.frame_current
        fcurve = get_fcurve(shape_keys, self.key_name)
        remove = getattr(self, "_remove", False) or has_keyframe_at(fcurve, frame)

        if remove:
            try:
                shape_keys.keyframe_delete(data_path=kf_data_path(self.key_name), frame=frame)
                self.report({'INFO'}, "Keyframe removed: %s" % key.name)
            except RuntimeError:
                self.report({'WARNING'}, "No keyframe on this frame: %s" % key.name)
        else:
            shape_keys.keyframe_insert(data_path=kf_data_path(self.key_name), frame=frame)
            self.report({'INFO'}, "Keyframe inserted: %s" % key.name)

        self._remove = False
        return {'FINISHED'}


class SMK_OT_keyframe_active(Operator):
    bl_idname = "smk.keyframe_active"
    bl_label = "Keyframe Active Shape Keys"
    bl_description = ("Insert a keyframe at the current frame for every shape key "
                       "(across all categories/tabs) whose value is different from 0.0.\n"
                       "Ctrl+Click to also remove keyframes at the current frame from those keys")
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        self._remove = event.ctrl
        return self.execute(context)

    def execute(self, context):
        settings = context.scene.shapekey_manager
        obj = settings.target_object
        if not is_valid_target(obj):
            self.report({'ERROR'}, "Nenhum objeto alvo valido")
            return {'CANCELLED'}

        shape_keys = obj.data.shape_keys
        frame = context.scene.frame_current
        remove = getattr(self, "_remove", False)
        count = 0

        for key in shape_keys.key_blocks:
            if key.name == "Basis":
                continue
            if key.value == 0.0:
                continue
            if remove:
                try:
                    shape_keys.keyframe_delete(data_path=kf_data_path(key.name), frame=frame)
                    count += 1
                except RuntimeError:
                    pass
            else:
                shape_keys.keyframe_insert(data_path=kf_data_path(key.name), frame=frame)
                count += 1

        self._remove = False

        if count == 0:
            self.report({'INFO'}, "Nenhuma shape key ativa (valor != 0)")
        else:
            action = "removidos" if remove else "inseridos"
            self.report({'INFO'}, "%d keyframes %s" % (count, action))
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

def draw_detail_card(layout, context, settings, obj):
    if not (0 <= settings.category_keys_index < len(settings.category_keys)):
        return
    key_name = settings.category_keys[settings.category_keys_index].name
    key = obj.data.shape_keys.key_blocks.get(key_name)
    if key is None:
        return

    frame = context.scene.frame_current
    fcurve = get_fcurve(obj.data.shape_keys, key.name)
    keyed_now = has_keyframe_at(fcurve, frame)

    layout.label(text=key.name)

    value_row = layout.row(align=True)
    value_row.prop(key, "value", text="Value")

    kf_icon = 'DECORATE_KEYFRAME' if keyed_now else 'DECORATE_ANIMATE'
    kf = value_row.operator("smk.toggle_keyframe", text="", icon=kf_icon, depress=keyed_now)
    kf.key_name = key.name

    minmax = layout.row(align=True)
    minmax.prop(key, "slider_min", text="Min")
    minmax.prop(key, "slider_max", text="Max")


class SMK_PT_main_panel(Panel):
    bl_label = "Shape Keys Controller"
    bl_idname = "SMK_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Shape Keys"

    def draw(self, context):
        layout = self.layout
        settings = context.scene.shapekey_manager

        target_box = layout.box()
        col = target_box.column(align=True)

        row = col.row(align=True)
        row.prop(settings, "target_object", text="")
        row.operator("smk.use_active_object", text="", icon="EYEDROPPER")
        row.operator("smk.refresh", text="", icon="FILE_REFRESH")

        obj = settings.target_object
        if not is_valid_target(obj):
            layout.separator()
            box = layout.box()
            box.label(text="Select the FACE MESH", icon="ERROR")
            return

        sync_category_list(settings, obj)

        layout.separator()
        layout.prop(settings, "variant", expand=True)

        layout.separator()
        search_row = layout.row(align=True)
        search_row.prop(settings, "search_filter", text="", icon="VIEWZOOM")
        search_row.operator("smk.keyframe_active", text="", icon="KEY_HLT")

        layout.separator()
        layout.template_list(
            "SMK_UL_categories", "", settings, "categories",
            settings, "categories_index", rows=4,
        )

        layout.separator()

        if len(settings.category_keys) > 0:
            layout.template_list(
                "SMK_UL_shapekeys", "", settings, "category_keys",
                settings, "category_keys_index", rows=6,
            )

            layout.separator()
            draw_detail_card(layout, context, settings, obj)
        elif len(settings.categories) > 0:
            box = layout.box()
            box.label(text="No shape keys inside this category", icon="INFO")


# ---------------------------------------------------------------------------
# Registro
# ---------------------------------------------------------------------------

classes = (
    SMK_CategoryItem,
    SMK_ShapeKeyRef,
    SMK_PropertyGroup,
    SMK_UL_categories,
    SMK_UL_shapekeys,
    SMK_OT_use_active,
    SMK_OT_refresh,
    SMK_OT_reset_key,
    SMK_OT_reset_category,
    SMK_OT_toggle_keyframe,
    SMK_OT_keyframe_active,
    SMK_PT_main_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.shapekey_manager = PointerProperty(type=SMK_PropertyGroup)


def unregister():
    del bpy.types.Scene.shapekey_manager
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()