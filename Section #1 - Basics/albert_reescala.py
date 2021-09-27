import cv2 as cv

####################################################################################################
############################# COM LLEGIR IMATGES I VIDEOS ##########################################
####################################################################################################


def  canviarRessolucio(width,height):
    # NOMES PER LIVE VIDEO
    capture.set(3,height)
    capture.set(4,height)



def rescaleFrame(frame, scale=0.75):
    # PER LIVE VIDEO, FOTOS I VIDEOS
    width = int (frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


# photo
img = cv.imread('Resources/Photos/cat.jpg')
resized_image = rescaleFrame(img,0.2)
cv.imshow('Cat', resized_image)


# Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,0.2)

    cv.imshow('Video',frame)
    cv.imshow('Video Recaled', frame_resized)

    if cv.waitKey(20) % 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()