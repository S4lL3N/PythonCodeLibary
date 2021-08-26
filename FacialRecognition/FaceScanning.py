import os
import cv2
import numpy as np
from PIL import Image
import pickle

baseDir = os.path.dirname(os.path.abspath(__file__))
imageDir = os.path.join(baseDir, "ImagesDB")

haarCascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
yLabels = []
xTrains = []

# grabs all png and jpg files from the directory path
for root, dirs, files in os.walk(imageDir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            print(label, path)

            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_= label_ids[label]
            print(label_ids)

            #yLabels.append(label)
            #xTrains.append(path)

            # convert image to numpy array
            pil_image = Image.open(path).convert("L")  # grey scale
            image_array = np.array(pil_image, "uint8")
            print(image_array)
            faces = haarCascade.detectMultiScale(image_array, scaleFactor=1.1, minNeighbors=5, minSize=(35, 35))

            for (x, y, w, h) in faces:
                roi = image_array[y:y+h, x:x+w]
                xTrains.append(roi)
                yLabels.append(id_)


#print(yLabels)
#print(xTrains)

with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(xTrains, np.array(yLabels))
recognizer.save("trainner.yml")