import bpy
import re


SEPARATOR_NAME = "==== both ===="


def create_combined_shapekeys():
    obj = bpy.context.active_object

    if not obj or not obj.data.shape_keys:
        print("no object with shape keys were found")
        return

    shape_keys = obj.data.shape_keys.key_blocks
    pairs = {}

    for sk in shape_keys:
        name = sk.name

        if 'xrange' in name.lower() or 'yrange' in name.lower():
            continue

        if '_R(' in name or '_R[' in name or name.endswith('_R'):
            base_name = name.replace('_R(', '(').replace('_R[', '[').replace('_R', '', 1) if name.endswith(
                '_R') else name.replace('_R(', '(').replace('_R[', '[')
            if base_name not in pairs:
                pairs[base_name] = {}
            pairs[base_name]['R'] = sk

        elif '_L(' in name or '_L[' in name or name.endswith('_L'):
            base_name = name.replace('_L(', '(').replace('_L[', '[').replace('_L', '', 1) if name.endswith(
                '_L') else name.replace('_L(', '(').replace('_L[', '[')
            if base_name not in pairs:
                pairs[base_name] = {}
            pairs[base_name]['L'] = sk

    # only create separator + combined keys if there are valid pairs
    valid_pairs = {k: v for k, v in pairs.items() if 'L' in v and 'R' in v}

    if not valid_pairs:
        print("no _L/_R pairs found, nothing to do")
        return

    # --- separator ---
    if SEPARATOR_NAME in shape_keys:
        print(f"separator '{SEPARATOR_NAME}' already exists, skipping...")
    else:
        sep = obj.shape_key_add(name=SEPARATOR_NAME, from_mix=False)
        sep.value       = 0.0
        sep.mute        = True
        sep.lock_shape  = True
        sep.slider_min  = 0.0
        sep.slider_max  = 0.0
        print(f"created separator '{SEPARATOR_NAME}'")

    # --- combine pairs ---
    created_count = 0
    for base_name, pair in valid_pairs.items():
        combined_name = base_name

        if combined_name in shape_keys:
            print(f"shape key '{combined_name}' already exists dummy, skipping...")
            continue

        obj.shape_key_add(name=combined_name, from_mix=False)
        new_sk = shape_keys[combined_name]
        new_sk.value = 0.0

        sk_l = pair['L']
        sk_r = pair['R']

        for i, vert in enumerate(obj.data.vertices):
            delta_l = sk_l.data[i].co - shape_keys[0].data[i].co
            delta_r = sk_r.data[i].co - shape_keys[0].data[i].co
            new_sk.data[i].co = shape_keys[0].data[i].co + delta_l + delta_r

        created_count += 1
        print(f"created: {combined_name} (from {sk_l.name} + {sk_r.name})")

    print(f"\ndone — {created_count} shape key(s) created")


create_combined_shapekeys()