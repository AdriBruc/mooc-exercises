#!/usr/bin/env python
# coding: utf-8

# In[1]:


def DT_TOKEN():
    # todo change this to your duckietown token
    dt_token = "dt1-3nT8KSoxVh4MguD4tsyUyCkFy1F6NthugyqasqTDWjZTcEG-43dzqWFnWd8KBa1yev1g3UKnzVxZkkTbfUmFNyzEVE79mfDU2V4ms8MpsN4gxG96Jn"
    return dt_token

def MODEL_NAME():
    # todo change this to your model's name that you used to upload it on google colab.
    # if you didn't change it, it should be "yolov5"
    return "yolov5"

# In[2]:


def NUMBER_FRAMES_SKIPPED():
    # todo change this number to drop more frames
    # (must be a positive integer)
    return 5

# In[3]:


# `class` is the class of a prediction
def filter_by_classes(clas):
    # Right now, this returns True for every object's class
    # Change this to only return True for duckies!
    # In other words, returning False means that this prediction is ignored.
    return clas==0

# In[4]:


# `scor` is the confidence score of a prediction
def filter_by_scores(scor):
    # Right now, this returns True for every object's confidence
    # Change this to filter the scores, or not at all
    # (returning True for all of them might be the right thing to do!)
    return scor >= 0.5

# In[5]:


# `bbox` is the bounding box of a prediction, in xyxy format
# So it is of the shape (leftmost x pixel, topmost y pixel, rightmost x pixel, bottommost y pixel)
def filter_by_bboxes(bbox):
    # Like in the other cases, return False if the bbox should not be considered.
    x = bbox[2] - bbox[0]
    y = bbox[3] - bbox[1]
    return x*y >= 3200
