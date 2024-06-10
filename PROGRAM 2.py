# -*- coding: utf-8 -*-
"""
Created on Sun May 21 16:42:50 2023

@author: ARM

Aim:Write a program to show rotation, scaling, and translation of an image. 
"""

#SCALLING

# Scaling an Image :- Scaling operation increases/reduces size of an image. 

import cv2

FILE_NAME = 'lenna.png'

img = cv2.imread(FILE_NAME)
print(img.shape)

try:
    # Read image from disk.
    img = cv2.imread(FILE_NAME)
    import matplotlib.pyplot as plt
    # Get number of pixel horizontally and vertically.
    (height, width) = img.shape[:2]
    fig,axes=plt.subplots(nrows=2,ncols=2)
    ax=axes.ravel()
    # Specify the size of image along with interpolation methods.
    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC
    # is used for zooming.
    res = cv2.resize(img, (int(height / 2), int(width / 2)), interpolation = cv2.INTER_AREA)
    print(ax[0].imshow(img))
    print(ax[0].set_title('original'))
    
    print(ax[1].imshow(res))
    print(ax[1].set_title('rescaled'))
    # Write image back to disk.
    cv2.imshow('rescaled', res)
    cv2.imwrite('scaled.jpg', res)
except IOError:
    print ('Error while reading files !!!')



#ROTAING THE IMAGE
#Rotating an image :- Images can be rotated to any degree clockwise or 
#otherwise. We just need to define rotation matrix listing rotation point,
# degree of rotation and the scaling factor.



import cv2
import numpy as np

FILE_NAME = 'lenna.png'
try:
    # Read image from the disk.
    img = cv2.imread(FILE_NAME)
    
    # Shape of image in terms of pixels.
    (rows, cols) = img.shape[:2]
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(nrows=2,ncols=2)
    ax=axes.ravel()
    # getRotationMatrix2D creates a matrix needed for transformation.
    # We want matrix for rotation w.r.t center to 45 degree without scaling.
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    res = cv2.warpAffine(img, M, (cols, rows))
    ax[0].imshow(img)
    ax[0].set_title("Orignal")
    
    ax[1].imshow(res)
    ax[1].set_title('rotated')
    # Write image back to disk.
    cv2.imshow('Rotated image',res)
    cv2.imwrite('rotated.jpg', res)
except IOError:
	print ('Error while reading files !!!')


# TRANSLATION OF IMAGE
# Translating an Image :- Translating an image means shifting it within a given
#frame of reference. 

import cv2

FILE_NAME = 'lenna.png'
# Create translation matrix.
# If the shift is (x, y) then matrix would be
# M = [1 0 x]
#	 [0 1 y]
# Let's shift by (100, 50).
M = np.float32([[1, 0, 100], [0, 1, 50]])

try: 
    # Read image from disk.
    img = cv2.imread(FILE_NAME)
    (rows, cols) = img.shape[:2]
    
    # warpAffine does appropriate shifting given the
    # translation matrix.
    res = cv2.warpAffine(img, M, (cols, rows))
    
    # Write image back to disk.
    cv2.imshow('Translated image',res)
    cv2.imwrite('translated.jpg', res)

except IOError:
	print ('Error while reading files !!!')
