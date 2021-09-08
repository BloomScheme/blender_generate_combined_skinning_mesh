import bpy
from .addon_preferences import get_addon_preferences_value


class ADDONNAME_PT_MainPanel(bpy.types.Panel):
    """Asset Panel"""

    bl_label = "Asset"
    bl_idname = "ADDONNAME_PT_MainPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Category"
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        scene = context.scene


classes = [
    ADDONNAME_PT_MainPanel,
]


def register():
    for target_class in classes:
        bpy.utils.register_class(target_class)


def unregister():
    for target_class in classes:
        bpy.utils.unregister_class(target_class)
