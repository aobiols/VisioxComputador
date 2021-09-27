import cv2 as cv

####################################################################################################
############################# COM LLEGIR IMATGES I VIDEOS ##########################################
####################################################################################################

# Imatges soles
# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('Cat', img)
#cv.waitKey(0)

# Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# capture = cv.VideoCapture(0)   ----> LA MEVA PRIMERA CAMERA

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) % 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()