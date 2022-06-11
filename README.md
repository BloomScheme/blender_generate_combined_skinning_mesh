# Blender Generate Combined Skinning Mesh

for Blender 3.2.0

Generate combined skinning mesh from Armature's children.

- Objects which is Parented by Bone-Relative will be assigned 1.0 weight to its parent bone.
  - If Object has intermediate parent Objects, it refers their parent bone.
- Otherwise, all Weights are inherited.


アーマチュアの子を走査して、統合したスキニングメッシュを生成する。

- ボーン相対で親子づけされたオブジェクトはボーンに対してウェイト1.0で割り当てられる。
  - 中間にEmptyなどがある場合も、その親ボーンを参照してウェイトを割り当てる。
- そうではないメッシュはそのままウェイトを引き継ぐ。

## setup

install and activete `Generate Combined Skinning Mesh`

## usage

- Select `Armature` object.
- click `View3D > Menu > Object > Convert > Generate Combined Skinning Mesh`.
