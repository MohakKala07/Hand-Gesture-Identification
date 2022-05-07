# Hand-Gesture-Recognition

## About the project
Gesture recognition has been a very interesting problem in `Computer Vision` community for a long time. This is particularly due to the fact that segmentation of foreground object from a cluttered background is a challenging problem in real-time. The most obvious reason is because of the semantic gap involved when a human looks at an image and a computer looking at the same image. Humans can easily figure out what’s in an image but for a computer, images are just 3-dimensional matrices. It is because of this, computer vision problems remains a challenge.

## Problem statement

We are going to recognize hand gestures from a video sequence. To recognize these gestures from a `live video sequence`, we first need to take out the hand region alone removing all the unwanted portions in the video sequence. After segmenting the hand region, we then count the fingers shown in the video sequence to instruct a robot based on the finger count. Thus, the entire problem could be solved using 2 simple steps -

* Find and segment the hand region from the video sequence.
* Count the number of fingers from the segmented hand region in the video sequence.

## Project Requirements

* **_Hardware Interfaces_**:
 1. Hard Disk: The database connectivity requires a hardware configuration that is on-line. This makes it necessary to have a fast database system running on high rpm hard disk permitting complete data redundancy and back-up systems to support the primary goal of reliability.
 2. The system must interface with the standard output devise, keyboard and mouse to interact with this software.
