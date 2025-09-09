import cv2
import numpy as np


def pixel_counting(image_bgr):
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(image_hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(image_hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    red_pixel_count = int(np.count_nonzero(mask))
    return red_pixel_count


if __name__ == "__main__":
    image_path = 'img.png'
    image_bgr = cv2.imread(image_path)
    print(pixel_counting(image_bgr))


