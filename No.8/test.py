import cv2
import numpy as np
import pytesseract
from PIL import Image
import paddlehub as hub

COUNT = 0


def show_image(image):
    global COUNT
    cv2.imshow(f'image{COUNT}', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    COUNT += 1


for i in range(9):
    ocr = hub.Module(name="ch_pp-ocrv3", enable_mkldnn=True)
    result = ocr.recognize_text(images=[cv2.imread(f"./images/{i}.jpg")])
    print(result)
