bl_info = {
    "name": "Bone Scaler",
    "author": "KRAL 👑",
    "version": (1, 1),
    "blender": (4, 5, 0),
    "location": "View3D > Sidebar > Bone Scaler",
    "description": "Seçili kemik veya tüm kemiklerin B-Bone kalınlığını Edit Mode'da tek bir slider ile kontrol eder",
    "category": "Rigging",
}

import bpy

# Update fonksiyonu
def update_bone_size(self, context):
    obj = context.object
    if obj and obj.type == 'ARMATURE' and context.mode == 'EDIT_ARMATURE':
        bones = obj.data.edit_bones
        selected_bones = [b for b in bones if b.select]
        if selected_bones:
            for bone in selected_bones:
                bone.bbone_x = obj.data.bone_scale
                bone.bbone_z = obj.data.bone_scale
        else:
            for bone in bones:
                bone.bbone_x = obj.data.bone_scale
                bone.bbone_z = obj.data.bone_scale

# Armature property ekleme
bpy.types.Armature.bone_scale = bpy.props.FloatProperty(
    name="Bone Scale",
    description="B-Bone kalınlığını tek slider ile kontrol eder",
    default=0.05,
    min=0.01,
    max=1.0,
    update=update_bone_size
)

# Panel sınıfı
class BONE_PT_ScalerPanel(bpy.types.Panel):
    bl_label = "Bone Scaler"
    bl_idname = "BONE_PT_scaler_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Bone Scaler'

    @classmethod
    def poll(cls, context):
        return context.mode == 'EDIT_ARMATURE'

    def draw(self, context):
        layout = self.layout
        arm = context.object.data
        layout.prop(arm, "bone_scale")

# Register/Unregister
classes = [BONE_PT_ScalerPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Armature.bone_scale

if __name__ == "__main__":
    register()
