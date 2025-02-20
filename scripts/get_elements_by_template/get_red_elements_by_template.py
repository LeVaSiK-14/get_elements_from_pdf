import cv2
import numpy as np


def get_red_elements_by_template(image_path: str, template_path: str) -> None:
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 150, 150])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 150, 150])
    upper_red2 = np.array([180, 255, 255])

    mask_red1 = cv2.inRange(image_hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(image_hsv, lower_red2, upper_red2)

    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    image_red = cv2.bitwise_and(image, image, mask=mask_red)

    image_gray = cv2.cvtColor(image_red, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    image_gray_blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)
    template_gray_blurred = cv2.GaussianBlur(template_gray, (5, 5), 0)

    result = cv2.matchTemplate(image_gray_blurred, template_gray_blurred, cv2.TM_CCORR_NORMED)

    threshold = 0.71
    locations = np.where(result >= threshold)

    binary_result = np.uint8(result >= threshold) * 255

    contours, _ = cv2.findContours(binary_result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    num_matches = len(contours) - 1
    
    print(f"Количество найденных шаблонов: {num_matches}")

    for pt in zip(*locations[::-1]):
        cv2.rectangle(image, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

    cv2.imwrite('media/all_elements_contours/all_elements_contours_red.png', image)
