import os
import cv2
import numpy as np
from PIL import Image
import random

# Constants for image sizes
IMAGE_WIDTH = 100  # Image width in pixels
IMAGE_HEIGHT = 100  # Image height in pixels

# Ranges for generaiting red shades (R, G, B)
R_MIN = 200
R_MAX = 255
G_MIN = 0
G_MAX = 50
B_MIN = 0
B_MAX = 100

# Ranges for HSV filtering red color
HSV_RED_LOWER_1 = np.array([0, 100, 100])
HSV_RED_UPPER_1 = np.array([10, 255, 255])
HSV_RED_LOWER_2 = np.array([170, 100, 100])
HSV_RED_UPPER_2 = np.array([180, 255, 255])


def load_image(img_path: str) -> np.ndarray:
    """
    Loads the image from the specified path with a validity check.

    Args:
        img_path (str): the path to the image file.

    Returns:
        np.ndarray: An image in BGR format, or None if the download failed.
    """
    try:
        img = cv2.imread(img_path)
        if img is None:
            # Return None if the image could not be loaded
            return None
        return img
    except cv2.error as e:
        print(f"OpenCV error when loading image: {e}")
        return None


def create_image():
    """Creates an image with dimensions IMAGE_WIDTH x IMAGE_HEIGHT, 
        filled with random shades of red, and saves it.
    """
    img = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT))
    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            r = random.randint(R_MIN, R_MAX)
            g = random.randint(G_MIN, G_MAX)
            b = random.randint(B_MIN, B_MAX)
            img.putpixel((x, y), (r, g, b))
    img.save('img.png')
    print("The image 'img.png' has been successfully created.")


def pixel_counting(image_bgr: np.ndarray) -> int:
    """
    Counts the number of red pixels in the image.

    Args:
        image_bgr (np.ndarray): the loaded image in BGR format.

    Returns:
        int: The number of pixels that fall under the red color mask.
    """
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(image_hsv, HSV_RED_LOWER_1, HSV_RED_UPPER_1)
    mask2 = cv2.inRange(image_hsv, HSV_RED_LOWER_2, HSV_RED_UPPER_2)
    mask = cv2.bitwise_or(mask1, mask2)

    red_pixel_count = int(np.count_nonzero(mask))

    return red_pixel_count


def main():
    """
    Main function. It requests the path to the image, loads it,
    and outputs the number of red pixels.

    Raises:
        ValueError: If the image path is empty, the file does not exist, or the image cannot be loaded.
    """
    try:
        s = input("Enter image path: ").strip()
        # input validation
        if not s:
            raise ValueError("Image path cannot be empty.")
        if not os.path.isfile(s):
            raise FileNotFoundError(f"File '{s}' does not exist.")
        img = load_image(s)
        if img is None:
            raise ValueError(f"Could not open image: {s}")
        count = pixel_counting(img)
        print(f"Number of red pixels: {count}")
    except (ValueError, FileExistsError) as error:
        print(f"Error: {error}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # If you need to create an image, use create_image()
    main()
