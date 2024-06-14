import cv2


face_cascade = cv2.CascadeClassifier('default.xml')

for i in range(188):
    img = cv2.imread('frames/' + str(i) + '.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imwrite('annotated/' + str(i) + '.jpg', img)


