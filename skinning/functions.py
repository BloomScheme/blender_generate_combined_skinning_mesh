from typing import List
import bpy
from bpy.types import Object

from ..blender_lib.collection import get_or_create_collection, link_to_collection
from ..blender_lib.mesh import (
    generate_mesh_object,
    get_freezed_mesh_object,
    join_mesh_object_into,
    set_vertex_group,
)
from ..blender_lib.object import (
    deselect_all,
    filter_objects_by_type,
    get_ancestors,
    set_active_object,
)


def generate_combined_skinning_mesh(armature: Object):
    if armature.type != "ARMATURE":
        raise ValueError("select ARMATURE object.")

    bpy.ops.object.mode_set(mode="OBJECT")

    children: List[Object] = filter_objects_by_type(armature.children_recursive, "MESH")

    combined_mesh = generate_mesh_object("combined", [], [], [])
    deselect_all()
    set_active_object(armature)
    # context.scene.collection.children[0]にリンクしているが、それがview layerから除外されていると
    # RuntimeError: Error: Object 'combined' can't be selected because it is not in View Layer 'View Layer'!
    # になるのでその時はscene collection直下にもリンクする
    if not combined_mesh.visible_get(view_layer=bpy.context.view_layer):
        scene_collection = bpy.context.scene.collection
        scene_collection.objects.link(combined_mesh)
        combined_mesh.select_set(True)
        bpy.ops.object.parent_set(type="ARMATURE_NAME")
    else:
        combined_mesh.select_set(True)
        bpy.ops.object.parent_set(type="ARMATURE_NAME")

    mech_mesh_collection = get_or_create_collection("Combined Skinning Mesh")
    link_to_collection(mech_mesh_collection, armature)
    link_to_collection(mech_mesh_collection, combined_mesh)

    for child in children:
        if child.hide_get():
            continue

        isHardObject = child.parent_type == "BONE" and child.parent_bone != None
        group_name = child.parent_bone

        ancestors = get_ancestors(child)
        for ancestor in ancestors:
            if ancestor.parent_type == "BONE" and ancestor.parent_bone != None:
                isHardObject = True
                group_name = ancestor.parent_bone
                break

        freezed = get_freezed_mesh_object(child)

        if freezed is None:
            continue

        if isHardObject:
            set_vertex_group(
                freezed, group_name, list(range(len(freezed.data.vertices))), 1.0
            )

        join_mesh_object_into(freezed, combined_mesh)
    
    set_active_object(armature)
    combined_mesh.select_set(True)
