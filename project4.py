import cv2
import pytesseract

# Path to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read image
img = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Extract text
text = pytesseract.image_to_string(gray)

print("Recognized Text:")
print(text)