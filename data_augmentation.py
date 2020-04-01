import cv2
import random
import argparse
import imutils
import os
import numpy as np

AMOUNT = 10
CROP_SIZE = 256
IMG_NAME = 'snow'
FILE_NAME = 'snow.png'


def crop(shape, img):
    '''
        Create new sub-parts of an image with a dimension suitable for AlexNet
    '''
    taken_points = []
    for i in range(AMOUNT):
        # Create new random starting point for cropped image
        # Make sure same point is not used more than once
        while True:
            ry, rx = random.randint(0, shape[1]-CROP_SIZE), random.randint(0,shape[0]-CROP_SIZE)
            if (ry, rx not in taken_points): break 
        taken_points.append((ry,rx)) 

        for r in range(rx, rx+256, 256):
            for c in range(ry, ry+256, 256):
                # Save new image
                cv2.imwrite(f"reshaped/{IMG_NAME}{i}.png", img[r:r+256, c:c+256,:])
                break

def rotate():
    '''
        Rotate every image in the directory, 90, 180 and 270 degrees
    '''
    # For every file in directory
    for img_name in os.listdir('./reshaped'):
        path = f'./reshaped/{img_name}'
        image = cv2.imread(path)    #Read image from path
        img_name = img_name[:-4]    #Strip file ending from filename
    
        # loop over the rotation angles
        rotation = 90 #Degrees
        for i in range(1,4):
            rotated = np.rot90(image,i)
            cv2.imwrite(f"reshaped/{img_name}_{rotation}.png", rotated)
            rotation += 90

def flip():
    '''
        Flip every image in the directory horizontally and vertically
    '''
    for img_name in os.listdir('./reshaped'):
        path = f'./reshaped/{img_name}'
        image = cv2.imread(path)    #Read image from path
        img_name = img_name[:-4]    #Strip file ending from filename

     # loop over the rotation angles
        
        flipped = np.flip(image, 1)
        cv2.imwrite(f"reshaped/{img_name}_flipped.png", flipped)


img = cv2.imread(FILE_NAME)
y, x = img.shape[0], img.shape[1]

crop((y,x), img)
rotate()
flip()