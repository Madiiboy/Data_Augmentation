import cv2
import random
import argparse
import imutils
import os

AMOUNT = 1
CROP_SIZE = 256
IMG_NAME = 'snow'
FILE_NAME = 'snow.png'


def crop(shape, img):
    '''
        Create new sub-parts of an image with a dimension suitable for AlexNet
    '''

    for i in range(AMOUNT):
        # Create new random starting point for cropped image
        ry, rx = random.randint(0, shape[1]-CROP_SIZE), random.randint(0,shape[0]-CROP_SIZE)  

        for r in range(rx, rx+256, 256):
            for c in range(ry, ry+256, 256):
                # Save new image
                cv2.imwrite(f"reshaped/{IMG_NAME}{i}.png", img[r:r+256, c:c+256,:])
                break

def rotateAll():
    '''
        Rotate every image in the directory, 90, 180 and 270 degrees
    '''
    # For every file in directory
    for img_name in os.listdir('./reshaped'):
        path = f'./reshaped/{img_name}'
        image = cv2.imread(path)    #Read image from path
        img_name = img_name[:-4]    #Strip file ending from filename
    
        # loop over the rotation angles
        rotation = 90
        for angle in range(90, 360, 90):
            rotated = imutils.rotate(image, angle)
            cv2.imwrite(f"reshaped/{img_name}_{rotation}.png", rotated)
            rotation += 90


img = cv2.imread(FILE_NAME)
y, x = img.shape[0], img.shape[1]

crop((y,x), img)
rotateAll()