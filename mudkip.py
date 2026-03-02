import cv2
import numpy as np
import matplotlib.pyplot as mp
import sys

np.set_printoptions(threshold = sys.maxsize)

##has cv2 read image and print as numpy array
mudkip = cv2.imread("/home/garrett/Downloads/mudkip.png",1)
###print(mudkip) prints numpy array

##prints image data using cv2 classes
print("img size", mudkip.shape)
print("data type of img", mudkip.dtype)

##resize image
small_mudkip = cv2.resize(mudkip,(32,32))

##displays image array
print(small_mudkip)

##uses matplotlib to plot image in orginal color
mp.imshow(small_mudkip)

##changes color channel matrix from bgr to rbg
small_mudkip_rbg = small_mudkip[:,:,::-1]
 
##prepares image to in plot
mp.imshow(small_mudkip_rbg)
mp.savefig("small_mudkip.png")

##shows aforementioned image
mp.show()

cv2.imread("/home/garrett/Documents/code/code.py/openCV_py/small_mudkip.png",cv2.IMREAD_COLOR)

##splits image into bgr
b,g,r = cv2.split(small_mudkip)

##shows channels
mp.figure(figsize = [20,5])

##shows specific channels
##red
mp.subplot(141);mp.imshow(r,cmap = "grey");mp.title("red")
mp.subplot(142);mp.imshow(g, cmap = "grey");mp.title('green')
mp.subplot(143);mp.imshow(b, cmap = "grey");mp.title('blue')

##all together
merged_mudkip = cv2.merge((b,g,r))

##show merged output
mp.subplot(144);mp.imshow(merged_mudkip[:,:,::-1])
mp.savefig("bgr.png")
mp.show()

##convert bgr mudkip into rbg from bgr components
color_covnerted = cv2.cvtColor(merged_mudkip, cv2.COLOR_BGR2RGB)
mp.imshow(color_covnerted)
mp.show()

##convert him to hsv now
small_mudkip_hsv = cv2.cvtColor(merged_mudkip, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(small_mudkip_hsv)

##plot hsv channels
##shows channels
mp.figure(figsize = [20,5])

##shows specific channels for hsv file and plots them
mp.subplot(141);mp.imshow(h,cmap = "grey");mp.title("h")
mp.subplot(142);mp.imshow(s, cmap = "grey");mp.title('s')
mp.subplot(143);mp.imshow(v, cmap = "grey");mp.title('v')
mp.subplot(144);mp.imshow(merged_mudkip, cmap = "grey"); mp.title("original")
mp.savefig("hsv.png")
mp.show()