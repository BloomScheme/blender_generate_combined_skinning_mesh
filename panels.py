import bpy

from .mech.operators import COMBINEDMECHMESH_OT_generate_combined_mech_mesh
from .addon_preferences import get_addon_preferences_value


class BLENDERCOMBINEDMECHMESH_PT_MainPanel(bpy.types.Panel):
    """Mech Tools Panel"""

    bl_label = "Mech Tools"
    bl_idname = "BLENDERCOMBINEDMECHMESH_PT_MainPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Mech Tools"
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.operator(COMBINEDMECHMESH_OT_generate_combined_mech_mesh.bl_idname)

classes = [
    BLENDERCOMBINEDMECHMESH_PT_MainPanel,
]


def register():
    for target_class in classes:
        bpy.utils.register_class(target_class)


def unregister():
    for target_class in classes:
        bpy.utils.unregister_class(target_class)
