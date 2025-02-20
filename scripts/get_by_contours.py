import cv2
import numpy as np

# Загружаем изображение
image = cv2.imread('media/drowing_images/extracted_drawing_27.png')

# Преобразуем изображение в HSV (цветовое пространство)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Диапазоны для синего цвета в HSV
lower_blue = np.array([100, 150, 150])
upper_blue = np.array([140, 255, 255])

# Диапазоны для красного цвета в HSV
lower_red1 = np.array([0, 150, 150])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 150, 150])
upper_red2 = np.array([180, 255, 255])

# Маска для синего цвета
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# Маска для красного цвета
mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Объединяем маски для красного
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

# Применяем маску на исходное изображение для синего
result_blue = cv2.bitwise_and(image, image, mask=mask_blue)

# Применяем маску на исходное изображение для красного
result_red = cv2.bitwise_and(image, image, mask=mask_red)

# Находим контуры для синего
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Находим контуры для красного
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Рисуем контуры для синего на изображении
# for cnt in contours_blue:
#     cv2.drawContours(result_blue, [cnt], -1, (0, 255, 0), 2)

# # Рисуем контуры для красного на изображении
# for cnt in contours_red:
#     cv2.drawContours(result_red, [cnt], -1, (0, 255, 0), 2)



cv2.imwrite(f'media/detect_elements/red_elements.png', result_red)
cv2.imwrite(f'media/detect_elements/blue_elements.png', result_blue)
