import inspect, os, sys, subprocess
import matplotlib.pyplot as plt
import numpy as np
import imageio
import cv2
import loader as do
ax = plt.figure().add_subplot(projection='3d')
# plt.ion()
# scanpath ='/home/gareth/Dropbox/Lola_WorkExperience/PythonCode/Processed/'
scanpath ='/home/gareth/Dropbox/Lola_WorkExperience/PythonCode/David_Processed/'
scannum = 136
rdata = np.array([[]]*17).T
#rchi,rx,ry, rz,ralpha, rbeta, rgamma, rm1, rm2, rm3, rm4, rm5,	rm6, z,y,z,x


for scannum in list(range(136,136+24,1)):
	rpos_plus_xzyz = np.loadtxt(scanpath+'scan_'+str(scannum))
	rdata = np.vstack((rdata,np.array(rpos_plus_xzyz)))


xyz = rdata[:,[-3,-1,-2]]
xyznorm = np.apply_along_axis(np.linalg.norm, 1, xyz)

ax.scatter(xyz[:,0],xyz[:,1],xyz[:,2])
ax.scatter(0,0,0)
plt.title('Robot Arm Sphere Error')

# ~ ax.xlabel('x (mm)')
# ~ ax.ylabel('y (mm)')
# ~ ax.zlabel('z (mm)')
plt.show()

# ~ np.savetxt("/home/gareth/Dropbox/Lola_WorkExperience/RobotArm/xyz.csv", xyz, delimiter=",")
# np.savetxt("/home/gareth/Dropbox/Lola_WorkExperience/RobotArm/xyz.dat", xyz)

plt.figure()
plt.plot(rdata[np.r_[0:384:16],7], xyz[np.r_[0:384:16],1], 'o')
# plt.plot(rdata[:,-2],'o')
# plt.plot(rdata[:,-2],'+')
# plt.plot(rdata[:,-4],'x')
# plt.plot(rdata[:,-4],'s')
plt.show()


