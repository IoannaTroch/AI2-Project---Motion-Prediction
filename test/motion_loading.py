from ai4animation import Motion

# Load from different formats
glb_motion = Motion.LoadFromGLB("character.glb", names=bone_names, floor=None)
# fbx_motion = Motion.LoadFromFBX("character.fbx") # requires Autodesk FBX SDK Python bindings to run
bvh_motion = Motion.LoadFromBVH("character.bvh", scale=0.01) # scale=0.01 converts cm to m

# Load from the internal NPZ format
npz_motion = Motion.LoadFromNPZ("character.npz") # internal motion format
# stores 7 dimensions (3D position + 4D quaternion) for each skeleton joint per frame

# Save any motion to NPZ
glb_motion.SaveToNPZ("character")