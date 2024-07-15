import cv2
import os
from settings import *

def face_detection(imagePath):
    global bbCenter
    """variable to open the image path"""
    img = cv2.imread(imagePath)
    """variable to store image converted to grayscale"""
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    """creates a CascadeClassidier object"""
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    """variable to store the image with facial recognition"""
    face = face_classifier.detectMultiScale(gray_image, scaleFactor=scaleFactorValue, minNeighbors=minNeighborsValue, minSize=minSizeValue)
    """creates the bounding box for facial recognition"""


    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), bbBoxColor, bbThickness)
        bbCenter = [int(y + (h / 2)), int(x + (w / 2))]

    """variable to convert image back to RGB"""
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # """show image with facial recognition"""
    # plt.figure(figsize=(20,10))
    # plt.imshow(img_rgb)
    # plt.show()
    # plt.axis('off')
    # print(bbCenter)

def crop_image(imagePath):
    img = cv2.imread(imagePath)
    # print (img.shape)
    global img_cropped
    img_cropped = img[0:3456, (bbCenter[1]-1728):(bbCenter[1]+1728)]
    # print(img_cropped.shape)
    os.chdir(temp_dir)
    filename = os.path.basename(imagePath)
    cv2.imwrite('temp_' + filename, img_cropped)

def resize_image(imagePath):
    img = cv2.imread(imagePath)
    img_resized = cv2.resize(img, (resizeWidth, resizeHeight))
    os.chdir(resized_image_dir)
    filename = (os.path.basename(imagePath)).replace('temp_', '')
    cv2.imwrite(filename, img_resized)
