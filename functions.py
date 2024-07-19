import cv2
import os
from settings import *


def image_formater(imagePath):
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

    img = cv2.imread(imagePath)
    img_cropped = img[0:3456, (bbCenter[1]-1728):(bbCenter[1]+1728)]
    os.chdir(temp_dir)
    filename = os.path.basename(imagePath)
    cv2.imwrite('temp_' + filename, img_cropped)
    temp_image = ('temp_' + filename)

    img = cv2.imread(temp_image)
    img_resized = cv2.resize(img, (resizeWidth, resizeHeight))
    os.chdir(resized_image_dir)
    filename = (os.path.basename(temp_image)).replace('temp_', '')
    cv2.imwrite(filename, img_resized)

def delete_files_in_directory(directory_path):
    files = os.listdir(directory_path)
    for file in files:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

