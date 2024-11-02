#  Text Detection and Extraction

import cv2
import pytesseract
import numpy as np

# Path to the Tesseract executable (Update this path as necessary)
pytesseract.pytesseract.tesseract_cmd = r'Users/shashank/Downloads/tesseract.pkg'

def preprocess_image(image_path):
    """
    Apply preprocessing to the image to prepare it for OCR.
    """
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    denoised_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    _, binary_image = cv2.threshold(denoised_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    normalized_image = cv2.equalizeHist(binary_image)
    coords = np.column_stack(np.where(normalized_image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    if angle != 0:
        (h, w) = normalized_image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        deskewed_image = cv2.warpAffine(normalized_image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    else:
        deskewed_image = normalized_image
    new_width = 800
    aspect_ratio = new_width / float(deskewed_image.shape[1])
    new_height = int(deskewed_image.shape[0] * aspect_ratio)
    resized_image = cv2.resize(deskewed_image, (new_width, new_height), interpolation=cv2.INTER_AREA)
    return resized_image

def extract_text(image):
    """
    Extract text from the preprocessed image using Tesseract OCR.
    """
    # Configure Tesseract for OCR
    custom_config = r'--oem 3 --psm 6'  # OEM 3: Default, PSM 6: Assume a single uniform block of text
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

def main():
    image_path = 'path_to_your_image.png'  # Update this path
    preprocessed_image = preprocess_image(image_path)
    text = extract_text(preprocessed_image)
    print("Extracted Text:")
    print(text)

if __name__ == "__main__":
    main()