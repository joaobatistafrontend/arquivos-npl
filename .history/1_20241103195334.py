import cv2
import pytesseract as pt
install = 'https://github.com/UB-Mannheim/tesseract/wiki'
caminho = 'C:\Program Files\Tesseract-OCR'

img = cv2.imread('img.png')
pt.pytesseract.tesseract_cmd = caminho + '\tesseract'
text = pt.image_to_string(img)
print(text)