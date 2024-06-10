# -*- coding: utf-8 -*-
"""
Created on Sun May 21 17:50:17 2023

@author: ARM

Aim:Read an image and extract and display low-level features such as edges,
textures using filtering techniques
"""
import cv2
import numpy as np

img=cv2.imread('lenna.png')

gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('grayscale image',gray)
cv2.imwrite('grayscale image.jpg',gray)
blur_gaussian=cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)

sobel_x=cv2.Sobel(blur_gaussian,cv2.CV_64F,1,0,ksize=5)

sobel_y=cv2.Sobel(blur_gaussian,cv2.CV_64F,0,1,ksize=5)

sobel_edges=cv2.addWeighted(sobel_x,0.5,sobel_y,0.5,0)

laplacian =cv2.Laplacian(blur_gaussian,cv2.CV_64F)

canny_edges =cv2.Canny(blur_gaussian,100,200)

cv2.imshow('Filtered Output',blur_gaussian)
cv2.imwrite('Filtered Output.jpg',blur_gaussian)

cv2.imshow('Sobel edge',sobel_edges)
cv2.imwrite('Sobel edge.jpg',sobel_edges)

cv2.imshow('Laplacian  ',laplacian)
cv2.imwrite('Laplacian .jpg ',laplacian)

cv2.imshow('Canny edge detection ',canny_edges)
cv2.imwrite('Canny edge detection.jpg ',canny_edges)

blur_median=cv2.medianBlur(gray,5)

cv2.imshow('Median Blur',blur_median)
cv2.imwrite('Median Blur.jpg',blur_median)

bilateral =cv2.bilateralFilter(gray,15,75,75)

cv2.imshow('Bilateral Filter',bilateral)
cv2.imwrite('Bilateral Filter.jpg',bilateral)

ksize=31
sigma=5
theta=0
lamda=10
gamma=0.5
phi=0
kernel =cv2.getGaborKernel((ksize,ksize),sigma,lamda,gamma,phi,ktype=cv2.CV_32F)

gabor=cv2.filter2D(gray,cv2.CV_8UC3,kernel)

cv2.imshow('Gabor filter',gabor)
cv2.imwrite('Gabor filter.jpg',gabor)
