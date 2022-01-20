import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat_1.jpeg")

# # Translation:
# def translate(img, x, y):
#     transMat = np.float([[1, 0, x], [0, 1, y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMat, dimensions)
#
# # -x --> Left
# # -y --> Up
# # x --> Right
# # y --> Down
#
#
# translated = translate(img, 100, 100)
# cv.imshow("translated", translated)

## ----------------------------------------

# # Rotation
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
#
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
#
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)
#
#     return cv.warpAffine(img, rotMat, dimensions)
#
# rotated = rotate(img, 45) # 45 is the angle
# cv.imshow("rotated", rotated)
## ----------------------------------------
# # Resizing
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow("resized", resized)
## ----------------------------------------
# # Flipping
# flip = cv.flip(img, 1)  # 0 flips vertically and 1 flips horizontally
# cv.imshow("flip", flip)
## ----------------------------------------


cv.waitKey(0)

