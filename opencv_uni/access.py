##access camera

import cv2
import sys

##selects 1 camera to use
s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

win_name = 'opencv preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27: 
##while loop that streams video as long as esc isn't pressed
    has_frame, frame = source.read() 
    if not has_frame: ##if some issue arises with the frames, then the camera shuts off
        break;
    cv2.imshow(win_name,frame) ##sends frames to output window

source.release()
cv2.destroyWindow(win_name)
