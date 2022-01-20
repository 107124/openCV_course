import cv2 as cv

## -------------------------------------
## How to read images:
# img = cv.imread('Photos/cat_2.jpeg')
#
# cv.imshow("Cat", img)
# cv.waitKey(0)

## -------------------------------------

## How to read videos:
## This is for your webcam
# capture = cv.VideoCapture(0)
capture = cv.VideoCapture("Videos/dog_1.mp4")

while True:
    isTrue, frame = capture.read()  # this reads the video frame by frame in the loop
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):  # if the letter 'd' is pressed then break out of the loop or wait 20 seconds
        break

capture.release()
cv.destroyAllWindows()

