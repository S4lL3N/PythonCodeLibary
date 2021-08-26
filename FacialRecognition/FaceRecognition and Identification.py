import numpy as np
import cv2
import pickle

windowName = "FaceRec & Identification"
cv2.namedWindow(windowName)

cam = cv2.VideoCapture(0)

haarCascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')
haarCascade2 = cv2.CascadeClassifier('Cascades/data/haarcascade_profileface.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
    labels = pickle.load(f)
    labels = {v: k for k, v in labels.items()}

pictureNumber = 0

if cam.isOpened():
    ret, frame = cam.read()
    # print(ret)
    # print(frame)
else:
    ret = False

while ret:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converts image to gray scale
    faces = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(35, 35))
    sideFace = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(35, 35))

    for (x, y, w, h) in faces:
        # draws rectangle around detected face
        colorOfRec = (0, 255, 0)  # BGR 0-255  (50, 50, 200) = red (255, 0, 0) = blue (0, 255, 0) = green
        stroke = 2  # thickness of rectangle
        startCord = (x, y)
        endCordX = x + w
        endCordY = y + h
        cv2.rectangle(frame, startCord, (endCordX, endCordY), colorOfRec, stroke)
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 200), 2)

        # Region of interest
        #print(x, y, w, h)
        roiGray = gray[y:y+h, x:x+w]  # (y cord start, y cord end)
        roiColor = frame[y:y + h, x:x + w]

        # recognizer
        id_, conf = recognizer.predict(roiGray)
        if conf >= 45 and conf <= 85:
            #print(id_)
            percentage = str(round(conf, 2))
            print(labels[id_], percentage)  # output to console
            # name and percentage show up on cam
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (0, 0, 0)
            stroke2 = 2
            cv2.putText(frame, name + " " + percentage, (x, y), font, 1, color, stroke2, cv2.LINE_AA)

        # write the image to the imageDB folder
        pictureNumber = pictureNumber + 1
        imageItem = "image." + str(pictureNumber) + ".png"
        #cv2.imwrite("ImagesDB/" + imageItem, roiGray)

    # show the frame
    cv2.imshow(windowName, frame)

    # for a color video feed uncomment
    # cv2.imshow(windowName, frame)

    # hit the ESC key to end Video Capture
    if cv2.waitKey(1) == 27:
        break

cam.release()