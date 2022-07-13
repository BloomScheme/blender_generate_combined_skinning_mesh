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
from .skinning import operators as skinning_operators


def register():
    skinning_operators.register()
    # panels.register()


def unregister():
    skinning_operators.unregister()
    # panels.unregister()


if __name__ == "__main__":
    register()
