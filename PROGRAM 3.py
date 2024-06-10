# -*- coding: utf-8 -*-
"""
Created on Sun May 21 17:23:48 2023

@author: ARM

Aim:Read an image, first apply erosion to the image and then subtract the
 result from the original.
 Demonstrate the difference in the edge image if you use dilation instead of
 erosion.
    
"""
import cv2
import numpy as np

#Reading the input image
img=cv2.imread('lenna.png')

#Taking a matrix of size 5 as the kernel

kernel=np.ones((5,5),np.uint8)

theshold_lower=100       #Lower threshold
threshold_upper=200      #Upper threshold

edges=cv2.Canny(img,theshold_lower,threshold_upper)

cv2.imshow('edge image',edges)
cv2.imwrite('edge image.jpg',edges)
#The first parameter is the original image
#Kernel is the matrix with which image is convolved.
#and third parameter is the number of the iterations
#which will determine how much you want to erode or dilate a given image

img_erosion=cv2.erode(img,kernel,iterations=1)
img_subtracted=cv2.subtract(img,img_erosion) 


cv2.imshow('Subtracted image',img_subtracted)
cv2.imwrite('Subtracted image.jpg',img_subtracted)

img_dilation=cv2.dilate(img,kernel,iterations=1)

cv2.imshow('Input image',img)
cv2.imshow('Erosion',img_erosion)
cv2.imshow('Dilation',img_dilation)

cv2.imwrite('Input.jpg',img)
cv2.imwrite('Erosion.jpg',img_erosion)
cv2.imwrite('Dilation.jpg',img_dilation)

erosion_edges=cv2.erode(edges,kernel,iterations=1)
dilation_edges=cv2.dilate(edges,kernel,iterations=1)

cv2.imshow('Edge Image using Erosion',erosion_edges)
cv2.imshow('Edge Image using dilation',dilation_edges)

cv2.imwrite('Edge Image using Erosion.jpg',erosion_edges)
cv2.imwrite('Edge Image using dilation.jpg',dilation_edges)



