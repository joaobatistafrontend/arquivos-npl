import cv2
import pytesseract as pt

img = cv2.imread('img.png')
caminho = 'C:\Program Files\Tesseract-OCR'
text = pt.image_to_string(img)
print(text)