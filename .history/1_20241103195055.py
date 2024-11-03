import cv2
import pytesseract as pt

caminho = 'C:\Program Files\Tesseract-OCR'
img = cv2.imread('img.png')
text = pt.image_to_string(img)
print(text)