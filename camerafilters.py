###camerafilters

import cv2
import sys
import numpy as np

##filter variable declaration
preview = 0
blur = 1
features = 2
edge = 3

feature_params = dict(maxCorners = 500, 
                      qualityLevel = 0.2, 
                      minDistance = 15,
                      blockSize = 9)

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

image_filter = preview
alive = True

win_name = "filters demo"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(s)

while alive:
    has_frame, frame = source.read(s)
    if not has_frame:
        break
    ##applies image filter variables to functional conditionals
    frame = cv2.flip(frame,1)
    if image_filter == preview:
        result = frame
    elif image_filter == edge:
        result = cv2.Canny(frame,80,150) ##frame, lower thresh, upper thresh
    elif image_filter == blur:
        result = cv2.blur(frame, (13,13))
    elif image_filter == features:
        result = frame
        frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_grey, **feature_params)
        if corners is not None:
             for x,y in np.float32(corners).reshape(-1,2):
                cv2.circle(result, (int(x),int(y)), 10, (0,255,0), 1)
    cv2.imshow(win_name, result)

    ##assigning keyboard keys to image filter variables
    key = cv2.waitKey(1)
    if key == ord("q") or key == ord("Q") or key ==27:
        alive = False
    elif key == ord("c") or key == ord("C"):
        image_filter = edge
    elif key == ord('b') or key == ord("B"):
        image_filter = blur
    elif key == ord("f") or key == ord('F'):
        image_filter = features
    elif key == ord("p") or key == ord("P"):
        image_filter = preview

source.release()
cv2.destroyWindow(win_name)
