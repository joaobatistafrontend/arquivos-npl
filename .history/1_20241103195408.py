import cv2
import pytesseract as pt
install = 'https://github.com/UB-Mannheim/tesseract/wiki'
caminho = r'C:\Program Files\Tesseract-OCR'

img = cv2.imread('img.png')
pt.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
text = pt.image_to_string(img)
print(text)