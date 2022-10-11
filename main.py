import os
import shutil
import tkinter
from tkinter import filedialog

#
# imagine = cv2.imread('Cat01.jpg', 3)
#
# # cv2.imshow('Imagine', imagine)
# # cv2.waitKey(0)
# window_name = 'Image'
# # font
# font = cv2.FONT_HERSHEY_SIMPLEX
# # org
# org = (50, 50)
#
# # fontScale
# fontScale = 1
# # Blue color in BGR
# color = (255, 0, 0)
#
# # Line thickness of 2 px
# thickness = 2
#
# # Using cv2.putText() method
# image = cv2.putText(imagine, 'Beuka Bianka', org, font,
#                     fontScale, color, thickness, cv2.LINE_AA)
#
# # Displaying the image
# cv2.imshow(window_name, image)
# # cv2.imshow('Imagine', imagine)
# cv2.waitKey(0)
# cv2.imwrite('imagine_scris.jpg',imagine)
import cv2
import imutils
import numpy as np
import yaml

with open("config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

root = tkinter.Tk()

images = []
img_file = tkinter.filedialog.askdirectory()
root.destroy()

# print(data['Algorithm'][0])
# for key, value in data.items():
#     print(key, value)
    # if key=="Sharpening":
    #     print(value['contrast'])

# val=[len(i) for i in data.values()]
# print(val)

i = 0

directory = img_file + "_" + "aug"

#if directory exists, delete it and make a new one
if os.path.exists(directory):
    shutil.rmtree(directory)
os.makedirs(directory)


# iterate over the folder and check every file if it's an jpg file
for image in os.listdir(img_file):
    if (image.endswith(".jpg")):
        i = i + 1
        images.append(image)
        img = cv2.imread(os.path.join(img_file, image))
        cv2.imshow("Initial Image", img)
        cv2.waitKey(0)
        for key, value in data.items():
            # print(key, value)
            if key == "Rotation":
                rotation_angle = value
                newimage = imutils.rotate(img, angle=rotation_angle)
                image_new_name = image[:-4] + "_" + key + "_" + str(i) + image[-4:]
                # print(imagine_noua)
                os.chdir(directory)
                cv2.imwrite(image_new_name, newimage)
                cv2.imshow("New image", newimage)
                cv2.waitKey(0)

            if key == "Contrast":
                image_new_name = image[:-4] + "_" + key + "_" + str(i) + image[-4:]

                # contrast = 1.5  # 1.5 #0.5 #1.3 #0.5
                contrast=value['contrast']
                brightness =value['brightness']  # -100 #-50 #-150
                imgA = img.copy()
                # imgA = imgA.astype('float32')
                imgA = (imgA * contrast + brightness).clip(0.0, 255.0)
                os.chdir(directory)
                cv2.imwrite(image_new_name, imgA)
                cv2.imshow("New image1", imgA)
                cv2.waitKey(0)

            if key== "Sharpening":
                image_new_name = image[:-4] + "_" + key + "_" + str(i) + image[-4:]
                kernel = np.array([[-1, -1, -1],
                                   [-1, 9, -1],
                                   [-1, -1, -1]])
                imgFiltered = cv2.filter2D(img, -1, kernel)  # -1 result has the same depth as the source
                os.chdir(directory)
                cv2.imwrite(image_new_name, imgFiltered)
                cv2.imshow("New image1", imgFiltered)
                cv2.waitKey(0)

            # else:
            #     print("The algorithm was not defined.")
            #     continue
