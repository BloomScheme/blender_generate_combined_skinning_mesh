from typing import Dict, Union
import bpy
import os

"""
    Addon設定に関する機能
"""

# https://docs.blender.org/api/blender_python_api_2_68_release/bpy.types.AddonPreferences.html
"""
    Addon設定関連機能
"""
class ADDONNAME_PresetPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    # models_directory: bpy.props.StringProperty(
    #     name="Models directory",
    #     subtype="FILE_PATH",
    # )

    def draw(self, context):
        # https://docs.blender.org/api/latest/bpy.types.UILayout.html
        layout = self.layout

        # 表示するプロパティ名を指定
        # layout.prop(self, "models_directory")


override_preferences = None


def set_override_preferences(preference: Dict):
    """テスト等で利用するための設定上書き機能

    Args:
        preference (Dict): 上書き用設定。すべての設定項目が必要な点に注意。
    """
    global override_preferences
    override_preferences = preference


def get_addon_preferences_value(key: str):
    """アドオン設定値を取得する

    Args:
        key (str): 設定キー

    Raises:
        ValueError: アドオンが見つからなかった
        ValueError: 設定が見つからなかった

    Returns:
        Any: 設定された値。keyがなければNone。
    """
    # Addon設定は取得時に各所でNoneが発生する可能性があるのでメソッド化し処理
    # addon名は
    addon = bpy.context.preferences.addons.get(__package__)
    if addon is None:
        raise ValueError("no addon was found.")

    preferences = addon.preferences

    global override_preferences
    if override_preferences:
        preferences = override_preferences

    if preferences is None:
        raise ValueError("no preferences.")

    if key not in preferences:
        return None

    return preferences[key]

classes = [
    STAGINGMODELING_PresetPreferences,
]


def register():
    for target_class in classes:
        bpy.utils.register_class(target_class)


def unregister():
    for target_class in classes:
        bpy.utils.unregister_class(target_class)
