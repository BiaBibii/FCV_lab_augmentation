import os
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
import yaml

with open("config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

root = tkinter.Tk()

images = []
img_file = tkinter.filedialog.askdirectory()
root.destroy()
i = 0
# print(img_file)
directory = img_file + "_" + "aug"

# print(directory)
# check if the directory is created
if directory == None:
    os.mkdir(directory)

#iterate over the folder and check every file if it's an jpg file
for image in os.listdir(img_file):
    if (image.endswith(".jpg")):
        i = i + 1
        images.append(image)
        img = cv2.imread(os.path.join(img_file, image))
        cv2.imshow("Initial Image", img)
        cv2.waitKey(0)
        if data[0]['Algorithm'] == "Rotation":
            rotation_angle = int(data[0]['Parameters'])
            rot = imutils.rotate(img, angle=rotation_angle)
            imagine_noua = image[:-4] + "_" + data[0]['Algorithm'] + "_" + str(i) + image[-4:]
            # print(imagine_noua)
            os.chdir(directory)
            cv2.imwrite(
                imagine_noua, rot)
            cv2.imshow("New image", rot)
            cv2.waitKey(0)
        else:
            print("The algorithm was not defined.")
            break