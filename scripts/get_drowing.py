import cv2
import numpy as np
import os

from scripts.configs import *


def get_drowings(directory_path: str, directory_drowing_images_path: str) -> None:
    files = os.listdir(directory_path)
    files = [os.path.join(directory_path, f) for f in files if os.path.isfile(os.path.join(directory_path, f))]
    files.sort(key=lambda f: int(f.split('/')[-1].split('_')[1].split('.')[0]))

    for i, file in enumerate(files):
        print(file)
        
        image = cv2.imread(file)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([100, 150, 150])
        upper_blue = np.array([140, 255, 255])
        lower_red = np.array([0, 150, 150])
        upper_red = np.array([10, 255, 255])

        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_red = cv2.inRange(hsv, lower_red, upper_red)

        mask = cv2.bitwise_or(mask_blue, mask_red)

        result = cv2.bitwise_and(image, image, mask=mask)

        cv2.imwrite(f'{directory_drowing_images_path}/extracted_drawing_{i+1}.png', result)
