import os
import cv2
import PIL
import glob

frames = []

speed = 8

timelapse_img_dir = "Image"
image_list = []
image_dir = os.listdir(timelapse_img_dir)
for i in image_dir:
    if i.endswith(".jpeg"):
        image_list.append(i)

basepath = os.getcwd()
basepath = os.path.join(basepath, timelapse_img_dir)
print("Starting reading")
for i in image_list:
    filepath = os.path.join(basepath, i)
    # print(filepath)
    img = cv2.imread(filepath)
    # scale = 60
    # width = int(img.shape[1] * scale / 100)
    # height = int(img.shape[0] * scale / 100)
    # dim = (width, height)
    # # resize image
    # resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    frameSize = (img.shape[1], img.shape[0])
    break

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 30, frameSize)

for i in image_list:
    filepath = os.path.join(basepath, i)
    # print(filepath)
    img = cv2.imread(filepath)
    out.write(img)

print("Finsihed writing")
out.release()




