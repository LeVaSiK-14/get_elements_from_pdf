import cv2
import numpy as np
from scripts.configs import(
    BLUE, RED, UNKNOWN
)


def get_color_from_template(template_path: str) -> str:
    template = cv2.imread(template_path)
    template_hsv = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 150, 150])
    upper_blue = np.array([140, 255, 255])

    lower_red1 = np.array([0, 150, 150])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 150, 150])
    upper_red2 = np.array([180, 255, 255])

    mask_blue = cv2.inRange(template_hsv, lower_blue, upper_blue)
    mask_red1 = cv2.inRange(template_hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(template_hsv, lower_red2, upper_red2)

    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    avg_hue_blue = np.mean(template_hsv[:, :, 0][mask_blue > 0]) if np.sum(mask_blue) > 0 else None
    avg_hue_red = np.mean(template_hsv[:, :, 0][mask_red > 0]) if np.sum(mask_red) > 0 else None

    if avg_hue_blue is not None and 100 <= avg_hue_blue <= 140:
        return BLUE
    elif avg_hue_red is not None and ((0 <= avg_hue_red <= 10) or (170 <= avg_hue_red <= 180)):
        return RED
    else:
        return UNKNOWN
