import os
import tkinter
from tkinter import filedialog
import yaml

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

with open("config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
# print(data)

# print()

images = []
# def select_folder():
root = tkinter.Tk()
# images=[]
img_file = tkinter.filedialog.askdirectory()
root.destroy()
i=0
for image in os.listdir(img_file):
    if (image.endswith(".jpg")):
        i=i+1
        # print(i)
        # print(image)
        images.append(image)
        # print(image)
        img=cv2.imread(os.path.join(img_file, image))
        cv2.imshow("sdf",img)
        cv2.waitKey(0)
        if data[0]['Algorithm']=="Rotation":
            rotation=int(data[0]['Parameters'])
            rot = imutils.rotate(img, angle=rotation)
            imagine_noua=image+"_"+str(i)
            # print("imaigine nou   ",imagine_noua)
            cv2.imwrite('imagine_noua.jpg', rot)
            cv2.imshow("sdf", rot)
            cv2.waitKey(0)
        else:
            print("The algorithm was not defined.")
            break
# print(images)

# print(data[0]['Algorithm'])
# for images in os.listdir(img_file):
#     if (images.endswith(".png")):
#         print(images)

# def load_images_from_folder(folder):
#     images = []
#     for filename in os.listdir(folder):
#         img = cv2.imread(os.path.join(folder, filename))
#         cv2.imshow("ws", img)
#         cv2.waitKey(0)
#         # img = cv2.rotate(img, cv2.ROTATE_15)
#         rot = imutils.rotate(img, angle=15)
#         cv2.imshow("Imagine rotita", rot)
#         cv2.waitKey(0)
#         if img is not None:
#             images.append(img)
#     return images

# if __name__ == "__main__":
    # root = tkinter.Tk()
    # img_file = tkinter.filedialog.askopenfilename(initialdir=".", title="Select image file",
    #                                               filetypes=(("Image files", "*.jpg;*.png"), ("all files", "*.*")))
    # root.destroy()
    # img=cv2.imread(img_file)
    # cv2.imshow("sd",img)
    # cv2.waitKey(0)
    # select_folder()
    # load_images_from_folder("C:\\Users\\beuka\\UPT\\_masterAn1sem1\\FCV\\Lab\\Pictures")