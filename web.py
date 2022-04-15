# Python program to take
# screenshots


import numpy as np
import cv2
import pyautogui
import time

# take screenshot using pyautogui
for count in range(15):
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    cv2.imwrite("input/image1.png", image)
