import bpy
import os
from mathutils import Vector

class ADDONNAME_OT_sample_operator(bpy.types.Operator):
    """サンプルオペレータ"""

    bl_idname = "addonname.sample_operator"
    bl_label = "sample_operator"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return {"FINISHED"}


classes = [
    ADDONNAME_OT_sample_operator,
]


def register():
    for target_class in classes:
        bpy.utils.register_class(target_class)


def unregister():
    for target_class in classes:
        bpy.utils.unregister_class(target_class)
