import cv2
import pytesseract as pt

img = cv2.imread('img.png')
text = pt.image_to_string(img)
caminho = C:\Program Files\Tesseract-OCR
print(text)