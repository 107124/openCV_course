import cv2 as cv

# -------------------------------------
# How to resize images of different sizes:
# img = cv.imread('Photos/cat_2.jpeg')
#
# cv.imshow("Cat", img)

# This function is for a video that already exists and for resizing it. If you want live video resizing, scroll down.
def rescaleFrame(frame, scale = 0.75):  # this scale is going to make it 75% of the original size
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.waitKey(0)

capture = cv.VideoCapture("Videos/dog_1.mp4")

while True:
    isTrue, frame = capture.read()  # this reads the video frame by frame in the loop
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):  # if the letter 'd' is pressed then break out of the loop or wait 20 seconds
        break

capture.release()
cv.destroyAllWindows()

# This will resize only live video like your webcam:
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


