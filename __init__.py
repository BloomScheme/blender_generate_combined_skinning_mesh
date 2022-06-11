bl_info = {
    "name": "Generate Combined Skinning Mesh",
    "author": "Yusuke Sanekata",
    "version": (1, 0, 0),
    "blender": (3, 2, 0),
    "location": "View3D > Menu > Object > Convert > Generate Combined Skinning Mesh",
    "description": "",
    "warning": "",
    "doc_url": "",
    # "category": "Add Mesh",
}

import imp
from . import addon_preferences
from . import module_template
from .skinning import operators as mech_operators


def register():
    mech_operators.register()
    # panels.register()


def unregister():
    addon_preferences.unregister()
    module_template.unregister()
    # panels.unregister()


if __name__ == "__main__":
    register()
