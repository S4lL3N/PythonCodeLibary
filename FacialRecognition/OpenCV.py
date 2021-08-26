import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

# ----------------------------------------------------------------------------------------------------------------------
# Check OpenCV version
# print(cv2.__version__)
# ----------------------------------------------------------------------------------------------------------------------


def displayAImage():
    # opens a image on the SDD/HDD
    imagePath = "C:\\Users\\Shae Allen\\Pictures\\Wallpaper\\floweroflife.jpg"
    img = cv2.imread(imagePath)

    # cv2.namedWindow('FOL', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('FOL', img)
    cv2.waitKey(0)

def webcamCaptureImage():
    # takes a picture with the web cam
    cam = cv2.VideoCapture(0)
    if cam.isOpened():
        ret,  frame = cam.read()
        #print(ret)
        #print(frame)
    else:
        ret = False

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.title('color image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    cam.release()

def webcamLiveFeed():
    windowName = "Python live Video Feed"
    cv2.namedWindow(windowName)
    cam = cv2.VideoCapture(0)

    # shows resolution
    print('Width : ' + str(cam.get(3)))
    print('Height : ' + str(cam.get(4)))

    # sets resolution
    #cam.set(3, 400)
    #cam.set(4, 300)

    # 720p
    #cam.set(3, 1024)
    #cam.set(4, 768)

    # max for c920
    #cam.set(3, 2304)
    #cam.set(4, 1536)

    # to check
    #print('Width : ' + str(cam.get(3)))
    #print('Height : ' + str(cam.get(4)))

    if cam.isOpened():
        ret, frame = cam.read()
        #print(ret)
        #print(frame)
    else:
        ret = False

    while ret:
        ret, frame = cam.read()
        # !!!! to convert the video feed to grayscale uncomment !!!
        #output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow(windowName, output)

        # for a color video feed uncomment
        cv2.imshow(windowName, frame)

        # hit the ESC key to end Video Capture
        if cv2.waitKey(1) == 27:
            break

    cam.release()

def videoRecToFile():
    windowName = "Python Recording live Video Feed"
    cv2.namedWindow(windowName)
    cam = cv2.VideoCapture(0)

    fileName = "C:\\Users\\Shae Allen\\PycharmProjects\\CITC\\OpenCVCaptures\\Output.avi"
    #codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    #codec = cv2.VideoWriter_fourcc('H', '2', '6', '4')
    codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    framerate = 30
    resolution = (640, 480)
    VideoFileOutput = cv2.VideoWriter(fileName, codec, framerate, resolution)


    if cam.isOpened():
        ret, frame = cam.read()
        #print(ret)
        #print(frame)
    else:
        ret = False

    while ret:
        ret, frame = cam.read()

        VideoFileOutput.write(frame)

        # !!!! to convert the video feed to grayscale uncomment !!!
        #output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow(windowName, output)

        # for a color video feed uncomment
        cv2.imshow(windowName, frame)

        # hit the ESC key to end Video Capture
        if cv2.waitKey(1) == 27:
            break

    VideoFileOutput.release()
    cam.release()

def trackingByColor():
    windowName = "Color Tracking"
    cv2.namedWindow(windowName)
    cam = cv2.VideoCapture(0)

    if cam.isOpened():
        ret, frame = cam.read()

    else:
        ret = False

    while ret:
        ret, frame = cam.read()
        # converts BGR image to a HSV format "Hue Saturation Value"
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # RED Tracking
        low = np.array([140, 150, 0])
        high = np.array([180, 255, 255])

        # BLUE Tracking
        #low = np.array([100, 50, 50)
        #high = np.array([140, 255, 255])

        # GREEN Tracking
        # low = np.array([40, 50, 50)
        # high = np.array([80, 255, 255])

        image_mask = cv2.inRange(hsv, low, high)

        #output = cv2.bitwise_and(frame, frame, mask=image_mask)

        cv2.imshow(windowName, image_mask)
        cv2.imshow("Original Feed", frame)

        # hit the ESC key to end Video Capture
        if cv2.waitKey(1) == 27:
            break

    cam.release()

def faceDetection():
    face_cascade = cv2.CascadeClassifier('C:\\Users\\Shae Allen\\PycharmProjects\\CITC\\Cascades\\data\\haarcascade_frontalface_alt2.xml')
    #face_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_default.xml')


    windowName = "Where's Shae"
    cv2.namedWindow(windowName)
    cam = cv2.VideoCapture(0)

    # shows resolution
    print('Width : ' + str(cam.get(3)))
    print('Height : ' + str(cam.get(4)))

    # sets resolution
    # cam.set(3, 400)
    # cam.set(4, 300)

    # 720p
    # cam.set(3, 1024)
    # cam.set(4, 768)

    # max for c920
    # cam.set(3, 2304)
    # cam.set(4, 1536)

    # to check
    # print('Width : ' + str(cam.get(3)))
    # print('Height : ' + str(cam.get(4)))

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
            #print(x, y, w, h)
            #roi_gray = gray[y:y+h, x:x+w]

        cv2.imshow(windowName, frame)

        # for a color video feed uncomment
        #cv2.imshow(windowName, frame)

        # hit the ESC key to end Video Capture
        if cv2.waitKey(1) == 27:
            break

    cam.release()





#displayAImage()
#webcamCaptureImage()
#webcamLiveFeed()
#videoRecToFile()
#trackingByColor()
faceDetection()


