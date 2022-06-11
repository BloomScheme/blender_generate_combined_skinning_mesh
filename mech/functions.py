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


def generate_mech_mesh(armature: Object):
    if armature.type != "ARMATURE":
        raise ValueError("select ARMATURE object.")

    bpy.ops.object.mode_set(mode="OBJECT")

    children: List[Object] = filter_objects_by_type(armature.children_recursive, "MESH")

    mech_mesh = generate_mesh_object("mech_mesh", [], [], [])
    deselect_all()
    set_active_object(armature)
    mech_mesh.select_set(True)
    bpy.ops.object.parent_set(type="ARMATURE_NAME")

    mech_mesh_collection = get_or_create_collection("mech_mesh")
    link_to_collection(mech_mesh_collection, armature)
    link_to_collection(mech_mesh_collection, mech_mesh)

    for child in children:
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

        join_mesh_object_into(freezed, mech_mesh)
