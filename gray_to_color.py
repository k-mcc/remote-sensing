# convert gray image to color format.

import cv2

gray = cv2.imread("s_03334301_tiff.tif")
cv2.imshow('image', gray)
backtorgb = gray[:,:,::-1] 
#backtorgb = cv2.cvtColor(gray,cv2.COLOR_BGR2RGB)
cv2.imwrite("s_03334301.tif", backtorgb)


