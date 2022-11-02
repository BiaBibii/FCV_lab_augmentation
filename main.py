import os
import shutil
import tkinter
from tkinter import filedialog

import cv2
import imutils
import numpy as np
import yaml
from PIL import Image
# from PIL.Image import Transpose

with open("config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

root = tkinter.Tk()

images = []
img_file = tkinter.filedialog.askdirectory()
root.destroy()

i = 0

directory = img_file + "_" + "aug"

#if directory exists, delete it and make a new one
if os.path.exists(directory):
    shutil.rmtree(directory)
os.makedirs(directory)

def write_img(directory, image_new_name, new_image):
    os.chdir(directory)
    cv2.imwrite(image_new_name, new_image)

# iterate over the folder and check every file if it's an jpg file
for image in os.listdir(img_file):
    if (image.endswith(".jpg")):
        images.append(image)
        img = cv2.imread(os.path.join(img_file, image))

        cv2.imshow("Initial Image", img)
        cv2.waitKey(0)
        newimage = img.copy()
        for key, value in data.items():
            if key == "Rotation":
                rotation_angle = value
                i = i + 1
                newimage = img.copy()
                newimage = imutils.rotate(newimage, angle=rotation_angle)
                image_new_name = image[:-4] + "_" + key + "_" + str(i) + image[-4:]
                write_img(directory,image_new_name,newimage)
            if key == "Contrast":
                i = i + 1
                image_new_name = image[:-4] + "_" + key + "_" + str(i) + image[-4:]
                contrast=value['contrast']
                newimage = img.copy()
                newimage = newimage.astype('float32')
                newimage = (newimage * contrast).clip(0.0, 255.0)
                write_img(directory,image_new_name,newimage)
                
            if key == "Brightness":
                i = i + 1
                image_new_name = image[:-4] + "_" + key + "_" + str(i) + image[-4:]
                brightness =value['brightness']
                newimage = img.copy()
                newimage = newimage.astype('float32')
                newimage = (newimage + brightness).clip(0.0, 255.0)
                write_img(directory,image_new_name,newimage)

            if key== "Sharpening":
                i = i + 1
                image_new_name = image[:-4] + "_" + key + "_" + str(i) + image[-4:]
                newimage = img.copy()
                kernel = np.array([[-1, -1, -1],
                                   [-1, 9, -1],
                                   [-1, -1, -1]])
                # kernel=value['kernel']
                newimage = cv2.filter2D(newimage, -1, kernel)  # -1 result has the same depth as the source
                write_img(directory,image_new_name,newimage)

            if key== "Resize":
                i = i + 1
                image_new_name = image[:-4] + "_" + key + "_" + str(i) + image[-4:]
                newimage = img.copy()
                newimage = cv2.resize(newimage, (value['height'],value['width']))
                # new_image=cv2.resize(newimage, None, fx=0.75, fy=0.75)
                write_img(directory,image_new_name,newimage)

            if key== "Flip":
                i = i + 1
                image_new_name = image[:-4] + "_" + key + "_" + str(i) + image[-4:]
                newimage = img.copy()
                newimage= cv2.flip(newimage, value)
                write_img(directory,image_new_name,newimage)

            if key=="Scaling":
                i = i + 1
                image_new_name = image[:-4] + "_" + key + "_" + str(i) + image[-4:]
                newimage = img.copy()
                alpha=0.2
                newimage1=np.array(newimage)
                write_img(directory, image_new_name, newimage1)

