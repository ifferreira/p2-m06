import cv2

cam = cv2.VideoCapture("la_cabra.mp4")

frameno = 0
while(True):
    ret, frame = cam.read()
    if ret:
        name = 'frames/' + str(frameno) + '.jpg'
        print('new frame captured...' + name)

        cv2.imwrite(name, frame)
        frameno += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()

