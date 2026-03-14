###hdr video
##not mudkip this time

import os
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from urllib.request import urlretrieve
from zipfile import ZipFile

url = r"https://www.dropbox.com/s/qa1hsyxt66pvj02/opencv_bootcamp_assets_NB10.zip?dl=1"
savepath = os.path.join(os.getcwd(), "/home/garrett/Documents/code/code.py/openCV_py/opencv_bootcamp_assets_NB10.zip")
picture_path = Path(r"/home/garrett/Documents/code/code.py/openCV_py")
#print(picture_path)

#import zip file function
def download_unzip(url, savepath):
    """Download and unzip a file from a url and save to a path"""
    print(f"Downloading {url} to {savepath}...")
    urlretrieve(url, savepath)

    try: 
        with ZipFile(savepath) as z:
            z.extractall(os.path.split(savepath)[0])
        print("it is done correctly")
    except Exception as e:
        print("\nInvalid file", e)

#if not os.path.exists(savepath):
   # download_unzip(url, savepath)
#else:
    #print("it is already there")


def readImagesAndTimes():
    filenames = ["img_0.033.jpg", "img_0.25.jpg", "img_2.5.jpg", "img_15.jpg"]
    times = np.array([1 / 30, .25, 2.5, 15], dtype = np.float32)
    image =[]
    for filename in filenames:
        im = cv2.imread(filename)
        image.append(im)
    return image, times

image, times = readImagesAndTimes()

alignMTB = cv2.createAlignMTB()
alignMTB.process(image, image)
 
##debevec algorithm to plot pixel value over time
calibrateDebevec = cv2.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(image, times)

x = np.arange(256, dtype = np.uint8)
y = np.squeeze(responseDebevec)

ax = plt.figure(figsize = (30,10))
plt.title("Debevec Inverse Camera Response Function", fontsize=24)
plt.xlabel("Measured Pixel Value", fontsize=22)
plt.ylabel("Calibrated Intensity", fontsize=22)
plt.xlim([0, 260])
plt.grid()
plt.plot(x, y[:, 0], "b", x, y[:, 1], "g", x, y[:, 2], "r")
plt.show()

mergeDebevec = cv2.createMergeDebevec()
hdrDebevec = mergeDebevec.process(image, times, responseDebevec)

tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
ldrDrago = tonemapDrago.process(hdrDebevec)
ldrDrago = 3*ldrDrago

cv2.imwrite("ldr-Drago.jpg", 255*ldrDrago)

plt.figure(figsize = (20,10))
plt.imshow(np.clip(ldrDrago, 0, 1)[:,:,::-1])
plt.axis("off")
plt.show()