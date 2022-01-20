import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat_2.jpeg")
cv.imshow("Original", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# these will be displayed in grayscale but it's showing the high consecration of blue, green and red.
cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# lets merge these together
merged = cv.merge([b, g, r])
cv.imshow("Merged Image", merged)

cv.waitKey(0)