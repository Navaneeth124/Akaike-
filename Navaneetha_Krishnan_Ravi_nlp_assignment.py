#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install opencv-python


# In[ ]:


import cv2
import numpy as np


# In[ ]:


original_image = cv2.imread("C:\\Users\\seeyo\\Desktop\\Tasks Given by company\\data annotated\\original_image.jpg")
fully_annotated_image = cv2.imread("C:\\Users\\seeyo\\Desktop\\Tasks Given by company\\data annotated\\fully_annotated_image.jpg")


# In[ ]:


print('Original image shape:', original_image.shape)
print('Fully annotated image shape:', fully_annotated_image.shape)


# In[ ]:


original_image


# In[ ]:




def deannotate_image(original_image, fully_annotated_image):
    # Convert images to grayscale
    original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    fully_annotated_gray = cv2.cvtColor(fully_annotated_image, cv2.COLOR_BGR2GRAY)
    
    # Compute the difference between original and annotated images
    diff = cv2.absdiff(original_gray, fully_annotated_gray)

    # Threshold the difference image to obtain a binary mask
    mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Perform morphological operations to improve the mask
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Apply the mask to the annotated image to remove the annotations
    deannotated_image = cv2.bitwise_and(fully_annotated_image, fully_annotated_image, mask=mask)

    return deannotated_image

# Load original and annotated images
original_image = cv2.imread("C:\\Users\\seeyo\\Desktop\\Tasks Given by company\\data annotated\\original_image.jpg")
fully_annotated_image = cv2.imread("C:\\Users\\seeyo\\Desktop\\Tasks Given by company\\data annotated\\fully_annotated_image.jpg")

# Resize the fully annotated image to match the size of the original image
fully_annotated_image = cv2.resize(fully_annotated_image, (original_image.shape[1], original_image.shape[0]))

# Deannotate the image
deannotated_image = deannotate_image(original_image, fully_annotated_image)

# Display the results
cv2.imshow('Original Image', original_image)
cv2.imshow('Annotated Image', fully_annotated_image)
cv2.imshow('Deannotated Image', deannotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


# Display the results
cv2.imshow('Original Image', original_image)
cv2.imshow('Annotated Image', annotated_image)
cv2.imshow('Deannotated Image', deannotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

