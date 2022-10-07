import cv2


face_cascade = cv2.CascadeClassifier('face.xml')

# img = cv2.imread('test.jpg')
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    
    #convert image to grey scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # todo : learn more
    faces = face_cascade.detectMultiScale(gray, 1.05, 3)

    for x, y, w, h  in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()

