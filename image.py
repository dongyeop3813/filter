import cv2

from pathlib import Path
from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim


def compare_image(imageA, imageB):
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    score, diff = compare_ssim(grayA, grayB, full=True)

    if score > 0.72:
        return False
    else:
        return True

def cv2pil(img):
    color_converted = img[:, :, ::-1]
    pil_img = Image.fromarray(color_converted)
    return pil_img