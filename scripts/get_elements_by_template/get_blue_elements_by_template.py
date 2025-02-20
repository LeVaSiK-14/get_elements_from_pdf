import cv2
import numpy as np


def get_blue_elements_by_template(image_path: str, template_path: str) -> None:
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 150, 150])
    upper_blue = np.array([140, 255, 255])

    mask_blue = cv2.inRange(image_hsv, lower_blue, upper_blue)

    image_blue = cv2.bitwise_and(image, image, mask=mask_blue)

    image_gray = cv2.cvtColor(image_blue, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    kernel = np.ones((3, 3), np.uint8)
    image_gray_dilated = cv2.dilate(image_gray, kernel, iterations=1)
    template_gray_dilated = cv2.dilate(template_gray, kernel, iterations=1)

    result = cv2.matchTemplate(image_gray_dilated, template_gray_dilated, cv2.TM_CCOEFF_NORMED)


    # kernel = np.ones((5, 5), np.uint8)
    # mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)

    # image_gray_blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)
    # template_gray_blurred = cv2.GaussianBlur(template_gray, (5, 5), 0)

    # result = cv2.matchTemplate(image_gray_blurred, template_gray_blurred, cv2.TM_CCOEFF_NORMED)

    threshold = 0.873
    locations = np.where(result >= threshold)


    binary_result = np.uint8(result >= threshold) * 255

    contours, _ = cv2.findContours(binary_result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    num_matches = len(contours) -1
    
    print(f"Количество найденных шаблонов: {num_matches}")


    for pt in zip(*locations[::-1]):
        cv2.rectangle(image, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0, 255, 0), 2)

    cv2.imwrite('media/all_elements_contours/all_elements_contours_blue.png', image)
