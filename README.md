# CV-1-12

This script creates an image with red shades and counts the number of red pixels in the user-specified image using the OpenCV library.

## Capabilities

- Create an image sized 100×100 pixels with random shades of red (the sizes can be changed)
- Upload an image from a path entered by the user
- Count the number of red pixels in the uploaded image
- Check for the existence of the file and handle errors properly during the loading and processing of images

## Requirements
 - Python 3.x
 - Libraries:
     - opencv-python
     - numpy
     - Pillow

Installation of the necessary libraries:
```
pip install opencv-python numpy Pillow
```

## Usage

1. Run the script:
   ```
   python script_name.py
   ```
2. Enter the path to the image when prompted.
3. The script will output the number of red pixels in the image.

## Code structure

- `create_image()` — generates an image with red hues and saves it to the file `img_red.png`
- `load_image(img_path)` — loads the image with a validity check
- `pixel_counting(image_bgr)` — counts the red pixels in the image (in the HSV color space)
- `main()` — the main program loop with user input handling and error processing
