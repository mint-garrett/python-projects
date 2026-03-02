import cv2
import numpy as np
import matplotlib.pyplot as mp

small_mudkip = cv2.imread("/home/garrett/Documents/code/code.py/openCV_py/small_mudkip.png")

#mp imshow
mp.imshow(small_mudkip)
mp.title("mp")
mp.show()

##using openCV to display for 8 sec
w1 = cv2.namedWindow("win1") ##create display window
cv2.imshow(w1, small_mudkip) ###plots mudkip to window
cv2.waitKey(5000) ###displays window for 5k ms
cv2.destroyWindow(w1)

###  opencv display until key is pressed
w2= cv2.namedWindow("win2")
cv2.imshow(w2, small_mudkip)
cv2.waitKey(0)
cv2.destroyWindow(w2)
