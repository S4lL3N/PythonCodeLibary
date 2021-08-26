# takes 20 pictures in grayscale saves them to the imageDB folder
import cv2

windowName = "Image Database Generator"
cv2.namedWindow(windowName)
cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:\\Users\\Shae Allen\\PycharmProjects\\CITC\\Cascades\\data\\haarcascade_frontalface_alt2.xml')
sampleNumber = 0
id = input('Enter the name of person for recognition:')

if cam.isOpened():
    ret, frame = cam.read()
    # print(ret)
    # print(frame)
else:
    ret = False



while ret:
    ret, frame = cam.read()
    # !!!! to convert the video feed to grayscale uncomment !!!
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(35, 35))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 200), 2)

        sampleNumber = sampleNumber + 1

        cv2.imwrite("ImagesDB/" + id + '.' + str(sampleNumber) + ".jpeg", gray)
        cv2.imshow(windowName, frame)

    if cv2.waitKey(100) and 0xFF == ord('q'):
        break

    elif sampleNumber > 20:
        break

cam.release()
