import cv2 as cv

img = cv.imread("Photos/cat_2.jpeg")
cv.imshow("Original", img)

# Averaging:
average = cv.blur(img, (3,3))
cv.imshow("Average Blur", average)

# Gaussian Blur
guass = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian Blur", guass)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)

# Bilateral
bilaterial = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilaterial)

cv.waitKey(0)