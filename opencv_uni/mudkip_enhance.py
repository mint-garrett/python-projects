##mudkip image enhancement

import cv2
import numpy as np
import matplotlib.pyplot as mp
from PIL import Image
from IPython.display import Image

##scan in image and convert to rgb
mudkip_bgr = cv2.imread("/home/garrett/Documents/code/code.py/openCV_py/mudkip.png", cv2.IMREAD_COLOR)
mudkip_rbg = cv2.cvtColor(mudkip_bgr, cv2.COLOR_BGR2RGB)

##adding brightness
##create an nxn matrix where all entries are 50 to increase/decrease brightness
matrix = np.ones(mudkip_rbg.shape, dtype = "uint8") * 50
mudkip_rbg_bright = cv2.add(mudkip_rbg, matrix)
mudkip_rbg_dark = cv2.subtract(mudkip_rbg, matrix)

##show images
mp.imshow(mudkip_rbg_bright)
mp.show()
mp.imshow(mudkip_rbg_dark)
mp.show()

##changing contrast via multiplication
##create coefficient matrices
m1 = np.ones(mudkip_rbg.shape) * 8
m2 = np.ones(mudkip_rbg.shape)* 1.2

##need to use floating point to multiply them with cv2.multiply, then convert back to uint8
mudkip_rbg_lowC = np.uint8(cv2.multiply(np.float64(mudkip_rbg), m1))
mudkip_rbg_highC = np.uint8(cv2.multiply(np.float64(mudkip_rbg), m2))

mp.imshow(mudkip_rbg_lowC)
mp.show()
mp.imshow(mudkip_rbg_highC)
mp.show()

##image thresholding
mudkip_grey= cv2.imread("/home/garrett/Documents/code/code.py/openCV_py/mudkip.png", cv2.IMREAD_GRAYSCALE)
retval, mudkip_thresh = cv2.threshold(mudkip_grey, 0, 255, cv2.THRESH_BINARY)

mp.imshow(mudkip_grey)
mp.show()
mp.imshow(mudkip_thresh)
mp.show()

##bitwise operations

##scan em in as grayscale
mudkip_bgr_grey = cv2.imread("/home/garrett/Documents/code/code.py/openCV_py/mudkip_bgr.png", cv2.IMREAD_GRAYSCALE)
mp.figure(figsize = [20,5])
mp.subplot(121);mp.imshow(mudkip_bgr_grey, cmap = 'gray')
mp.subplot(122);mp.imshow(mudkip_grey, cmap = 'gray')
mp.show()

#bitwise and
and1 = cv2.bitwise_and(mudkip_bgr_grey, mudkip_grey, mask = None)
mp.imshow(and1, cmap = 'grey')
mp.show()

#bitwise or
or1 = cv2.bitwise_or(mudkip_bgr_grey, mudkip_grey, mask = None)
mp.imshow(or1, cmap = 'grey')
mp.show()

#bitwisexor
xor1 = cv2.bitwise_xor(mudkip_bgr_grey, mudkip_grey, mask = None)
mp.imshow(xor1, cmap = 'grey')
mp.show()

