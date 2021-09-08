import bpy
import os
from mathutils import Vector



classes = [
]


def register():
    for target_class in classes:
        bpy.utils.register_class(target_class)


def unregister():
    for target_class in classes:
        bpy.utils.unregister_class(target_class)
