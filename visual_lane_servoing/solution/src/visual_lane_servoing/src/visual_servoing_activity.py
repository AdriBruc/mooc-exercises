#!/usr/bin/env python
# coding: utf-8

# In[16]:


# The function written in this cell will actually be ran on your robot (sim or real). 
# Put together the steps above and write your DeltaPhi function! 
# DO NOT CHANGE THE NAME OF THIS FUNCTION, INPUTS OR OUTPUTS, OR THINGS WILL BREAK

import cv2
import numpy as np


def get_steer_matrix_left_lane_markings(shape):
    """
        Args:
            shape: The shape of the steer matrix (tuple of ints)
        Return:
            steer_matrix_left_lane: The steering (angular rate) matrix for Braitenberg-like control 
                                    using the masked left lane markings (numpy.ndarray)
    """
    
    quarter_x = int(shape[1]/4)
    tenth_y = int(shape[0]/10)
    steer_matrix_left_lane = np.zeros(shape)
    steer_matrix_left_lane[6*tenth_y:, :quarter_x] = -0.1
    steer_matrix_left_lane[3*tenth_y:, quarter_x:3*quarter_x] = -0.1
    
    return steer_matrix_left_lane

# In[17]:


# The function written in this cell will actually be ran on your robot (sim or real). 
# Put together the steps above and write your DeltaPhi function! 
# DO NOT CHANGE THE NAME OF THIS FUNCTION, INPUTS OR OUTPUTS, OR THINGS WILL BREAK


def get_steer_matrix_right_lane_markings(shape):
    """
        Args:
            shape: The shape of the steer matrix (tuple of ints)
        Return:
            steer_matrix_right_lane: The steering (angular rate) matrix for Braitenberg-like control 
                                     using the masked right lane markings (numpy.ndarray)
    """
    
    quarter_x = int(shape[1]/4)
    tenth_y = int(shape[0]/10)
    steer_matrix_right_lane = np.zeros(shape)
    steer_matrix_right_lane[6*tenth_y:, 3*quarter_x:] = 0.1
    steer_matrix_right_lane[3*tenth_y:, quarter_x:3*quarter_x] = 0.1
    
    return steer_matrix_right_lane

# In[18]:


# The function written in this cell will actually be ran on your robot (sim or real). 
# Put together the steps above and write your DeltaPhi function! 
# DO NOT CHANGE THE NAME OF THIS FUNCTION, INPUTS OR OUTPUTS, OR THINGS WILL BREAK

import cv2
import numpy as np


def detect_lane_markings(image):
    """
        Args:
            image: An image from the robot's camera in the BGR color space (numpy.ndarray)
        Return:
            left_masked_img:   Masked image for the dashed-yellow line (numpy.ndarray)
            right_masked_img:  Masked image for the solid-white line (numpy.ndarray)
    """
    
    h, w, _ = image.shape
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    sigma = 5
    img_gaussian_filter = cv2.GaussianBlur(img_gray,(0,0), sigma)
    sobelx = cv2.Sobel(img_gaussian_filter,cv2.CV_64F,1,0)
    sobely = cv2.Sobel(img_gaussian_filter,cv2.CV_64F,0,1)
    
    mask_left = np.ones(sobelx.shape)
    mask_left[:, int(w/2):] = 0
    mask_right = np.ones(sobelx.shape)
    mask_right[:, :int(w/2)] = 0
    
    threshold = 15
    Gmag = np.sqrt(sobelx*sobelx + sobely*sobely)
    mask_mag = (Gmag > threshold)
    
    mask_sobelx_pos = (sobelx > 0)
    mask_sobelx_neg = (sobelx < 0)
    mask_sobely_pos = (sobely > 0)
    mask_sobely_neg = (sobely < 0)

    white_lower_hsv = np.array([0, 0, 127])
    white_upper_hsv = np.array([179, 50, 255])
    yellow_lower_hsv = np.array([16, 50, 127])
    yellow_upper_hsv = np.array([32, 255, 255])
    mask_white = cv2.inRange(img_hsv, white_lower_hsv, white_upper_hsv)
    mask_yellow = cv2.inRange(img_hsv, yellow_lower_hsv, yellow_upper_hsv)
    
    mask_left_edge = mask_mag * mask_sobelx_neg * mask_sobely_neg * mask_yellow # mask_left *
    mask_right_edge = mask_mag * mask_sobelx_pos * mask_sobely_neg * mask_white # mask_right *
    
    return (mask_left_edge, mask_right_edge)
