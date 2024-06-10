 """
Created on Sun May 21 17:50:17 2023

@author: ARM

Aim:Demonstrate enhancing and segmenting low contrast 2D images.
"""

import cv2
import numpy as np

#Read the image

img=cv2.imread('lenna.png')

#cv2.cvtColor is applied over the image input with applied parameters
#to convert the image in grayscale

img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Apply histogram equalization to enhance the contrast openCV has a function to do
#this,cv2.equalizeHist()
#Its input is just grayscale image and output is our histogram equlaized image

img_equalize = cv2.equalizeHist(img_g)

#stacking images side-by-side

result =np.hstack((img_g,img_equalize))

#Apply otsu's thresholding method to segment the image
#Syntax:cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique)
#Parameters:
#   -> source:Input image array (must be in Grayscale).
#   -> thresholdValue:Value of Threshold below and
# above which pixel values will change accordingly.

ret,img_thresh =cv2.threshold(img_equalize, 0 ,255 ,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                                                                    
#Display the original image ,enhnaced image,enhanced image  
cv2.imshow("Original Image",img)
cv2.imwrite("Original Image.jpg",img)
cv2.imshow("Original Image Converted to grayscale",img_g)
cv2.imwrite("Original Image Converted to grayscale.jpg",img_g)
cv2.imshow("Enhanced Image",img_equalize)
cv2.imwrite("Enhanced Image.jpg",img_equalize)
cv2.imshow("Original Image & Enhanced Image ",result)
cv2.imwrite("Original Image & Enhanced Image.jpg ",result)
cv2.imshow("segmented Image",img_thresh)
cv2.imwrite("segmented Image.jpg",img_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
