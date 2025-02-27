import bpy
import fnmatch
import numpy as np
bpy.ops.object.select_all(action='DESELECT')
scene = bpy.context.scene

xyz = np.loadtxt('/home/gareth/Dropbox/Lola_WorkExperience/RobotArm/xyz.dat')
xyz = xyz/1000
xyz[:,2]=xyz[:,2]+0.352
for ii in range(xyz.shape[0]):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.00002, enter_editmode=False, align='WORLD', location=xyz[ii,:], scale=(1, 1, 1))
