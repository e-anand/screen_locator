import pyautogui
import time
import os

pyautogui.FAILSAFE = False


image_path = r'D:\Today\1.JPG'


def find_image_coordinates():
    location = pyautogui.locateOnScreen(image_path, confidence=0.8) 
    if location:
        return location.left, location.top
    else:
        return None

while True:
    image_coordinates = find_image_coordinates()
    if image_coordinates:
        print("Yes, the image is available at coordinates:", image_coordinates)
        x, y = image_coordinates
        pyautogui.click(x, y) 
    else:
        print("No, the image is not available.")
    

    time.sleep(5) 
