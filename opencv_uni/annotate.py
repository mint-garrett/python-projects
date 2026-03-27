##annotating images

import cv2
import numpy as np
import matplotlib.pyplot as mp
from PIL import Image
from IPython.display import Image

small_mudkip = cv2.imread("/home/garrett/Documents/code/code.py/openCV_py/small_mudkip.png", cv2.IMREAD_COLOR)
mp.imshow(small_mudkip[:,:,::-1])
mp.show()

##draw line on image
##[line start], [line end], (color)
small_mudkip_line = small_mudkip.copy()
cv2.line(small_mudkip_line, [20,100], [180,100], (0,255,255),thickness=6)
mp.imshow(small_mudkip_line[:,:,::-1])
mp.show()

##draw circle
##(radial  point), (radius)
small_mudkip_circle = small_mudkip.copy()
cv2.circle(small_mudkip_circle, (32,32), 200, (0,255,255), thickness = 7)
mp.imshow(small_mudkip_circle[:,:,::-1])
mp.show()

##draw rectangle
##(top left ocrner), (bottom right corner)
small_mudkip_rect = small_mudkip.copy()
cv2.rectangle(small_mudkip_rect,(32,32), (100,100), (255,0,255), thickness = 5)
mp.imshow(small_mudkip_rect[:,:,::-1])
mp.show()
