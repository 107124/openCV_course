import cv2 as cv

# -------------------------------------
# Basic Functions we use a lot in OpenCV:
img = cv.imread('Photos/cat_2.jpeg')

cv.imshow("Cat", img)

# -------------------------------------
# Converting to grayscale:
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Display the image:
cv.imshow("Gray", gray)

# -------------------------------------
# Bluring an image:
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)  # increase the tuple 7,7 to 10,10 etc. to make it more blurry
cv.imshow("Blur", blur)
# -------------------------------------
# Edge Cascade:
canny = cv.Canny(blur, 125, 175)  # to draw out less details, increase the blur
cv.imshow("canny", canny)
# -------------------------------------
# Dilating the image:
dilated = cv.dilate(canny, (7,7), iterations=1)  # iterations make the lines thicker
cv.imshow("dilated", dilated)
# -------------------------------------
# Eroding
eroded = cv.erode(dilated, (7,7), iterations=1)
cv.imshow("eroded", eroded)
# -------------------------------------
# Resize:
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)
# -------------------------------------
# Crop:
cropped = img[50:200, 200: 400]
cv.imshow("cropped", cropped)


cv.waitKey(0)
