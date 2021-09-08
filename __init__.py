bl_info = {
    "name": "",
    "author": "",
    "version": (0, 20, 1),
    "blender": (2, 93, 0),
    # "location": "View3D > Add > Mesh > New Object",
    "description": "",
    "warning": "",
    "doc_url": "",
    # "category": "Add Mesh",
}

from . import addon_preferences
from . import module_template
from . import panels


def register():
    addon_preferences.register()
    module_template.register()
    panels.register()


def unregister():
    addon_preferences.unregister()
    module_template.unregister()
    panels.unregister()


if __name__ == "__main__":
    register()
