# Blender Generate Combined Skinning Mesh

for Blender 3.2.0

Generate combined skinning mesh from Armature's children.

- Objects which is Parented by Bone-Relative will be assigned 1.0 weight to its parent bone.
  - If Object has intermediate parent Objects, it refers their parent bone.
- Otherwise, all Weights are inherited.

アーマチュアの子を走査して、統合したスキニングメッシュを生成する。

- ボーン相対で親子づけされたオブジェクトはボーンに対してウェイト 1.0 で割り当てられる。
  - 中間に Empty などがある場合も、その親ボーンを参照してウェイトを割り当てる。
- そうではないメッシュはそのままウェイトを引き継ぐ。

## setup

### download (for general users)

https://github.com/BloomScheme/blender_generate_combined_skinning_mesh/releases

### clone & init (for developers)

at addons directory:

```bash
git clone https://github.com/BloomScheme/blender_generate_combined_skinning_mesh.git
cd blender_generate_combined_skinning_mesh
git submodule update --init --recursive
```

### activate

on Blender: activate `Generate Combined Skinning Mesh`

## usage

- Select `Armature` object.
- click `View3D > Menu > Object > Convert > Generate Combined Skinning Mesh`.
