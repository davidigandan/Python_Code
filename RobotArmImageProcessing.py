import inspect, os, sys, subprocess
import matplotlib.pyplot as plt
import numpy as np
import imageio
import loader as do
plt.ion()
scanpath ='./datasetX/'
scannum = 599


imtemplate=str(scannum)+'-camlab84-files/%05d.tif'
imnum = 1
d = do.load(scanpath + str(scannum) + '.dat')

# ~ img = np.array(cv2.imread(str(scanpath + str(imtemplate % imnum)), cv2.IMREAD_GRAYSCALE))
# ~ edges = cv2.Canny(img,90,100)

# ~ plt.figure()
# ~ plt.imshow(img)
# ~ plt.show()

# ~ im1 = imageio.imread(str(scanpath + str(imtemplate % 1)))
# ~ im_array = np.zeros(im1.shape)
c3x, c3y = 236, 279 # cam3
c3x, c3y = c3y, c3x
c1x, c1y = 228, 430 # cam1
c1x, c1y = c1y, c1x

# ~ cx, cy = 319,699, 
maskdx, maskdy = 100, 100
roiindex = np.meshgrid(np.r_[c1x-maskdx:c1x+maskdx],np.r_[c1y-maskdy:c1y+maskdy])
roiindex2 = np.meshgrid(np.r_[c3x-maskdx:c3x+maskdx],np.r_[c3y-maskdy:c3y+maskdy])
# ~ kernel = im1[tuple(roiindex)].T
fig = plt.figure(figsize=(8, 8),dpi=130)
# ~ centres = np.array([[]]*17).T
xzyz = [0,0,0,0]
aa = [0,0,0,0]
imtemplate=str(scannum)+'-camlab84-files/%05d.tif'# cam1
imtemplate2=str(scannum)+'-camlab84b-files/%05d.tif'# cam1
for scannum in list(range(599,599+30,1)):
    d = do.load(scanpath + str(scannum) + '.dat')
    centres = np.array([[]]*17).T
    for imnum in d.path[list(range(0,d.path.shape[0],1))]:
        imnum = int(imnum)
        rpos = [d.rchi[imnum-1],	d.rx[imnum-1],	d.ry[imnum-1],	d.rz[imnum-1],	d.ralpha[imnum-1],	d.rbeta[imnum-1], d.rgamma[imnum-1], d.rm1[imnum-1],	d.rm2[imnum-1],	d.rm3[imnum-1],	d.rm4[imnum-1],	d.rm5[imnum-1],	d.rm6[imnum-1]]
        # im_array += imageio.imread(str(scanpath + str(imtemplate % imnum)))
        im = imageio.imread(str(scanpath + str(imtemplate % imnum)))
        plt.title(str(scannum))
        plt.imshow(im[roiindex].T)
        # ~ plt.imshow(im)
        a = plt.ginput(1,0)
        aa[0]=c1x-maskdx+int(a[0][1])
        aa[1]=c1y-maskdy+int(a[0][0])
        plt.clf()
        im = imageio.imread(str(scanpath + str(imtemplate2 % imnum)))
        plt.imshow(im[roiindex2].T)
        b = plt.ginput(1,0)
        aa[2]=c3x-maskdx+int(b[0][1])
        aa[3]=c3y-maskdy+int(b[0][0])
        plt.clf()
        #---------------------------------------------------------------
        #       Calculate error in pixels and convert to mm
        #---------------------------------------------------------------
        xzyz[0] = (aa[0] - c1x) * 0.0108
        xzyz[1] = (c1y - aa[1]) * 0.0108               
        xzyz[2] = (aa[2]- c3x) * 0.0125
        xzyz[3] = (c3y - aa[3]) * 0.0125
        rpos_plus_xzyz = rpos+xzyz
        
        centres = np.vstack((centres,np.array(rpos_plus_xzyz)))
    np.savetxt('scan_'+str(scannum),centres)
    
plt.close('all')

#rchi,	rx,	ry, rz,	ralpha, rbeta, rgamma, rm1, d.rm2, rm3, rm4, rm5,	rm6, x,z,y,z


