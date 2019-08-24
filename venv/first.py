import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd="C:\Program Files\Tesseract-OCR\Tesseract.exe"

img = cv2.imread("C:/Users/jayasurya/Desktop/images/111.jpg")
cv2.imshow("new", img)
cv2.waitKey(0)

text=pytesseract.image_to_string(img, lang='eng')
print(text)
