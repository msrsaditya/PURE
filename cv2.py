# Image Preprocessing

import cv2
import pytesseract
import numpy as np

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/Users/shashank/Downloads/tesseract.pkg'  # Update this path

def preprocess_image(image_path):
    # Load image
    image = cv2.imread(image_path)

    # Grayscale Conversion
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Noise Reduction
    denoised_image = cv2.medianBlur(gray_image, 3)  # Using median blur

    # Binarization
    _, binary_image = cv2.threshold(denoised_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Normalization (Optional: Adjust contrast and brightness)
    normalized_image = cv2.equalizeHist(binary_image)

    # Deskewing
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

    # Resizing
    new_width = 800  # Define desired width
    aspect_ratio = new_width / float(deskewed_image.shape[1])
    new_height = int(deskewed_image.shape[0] * aspect_ratio)
    resized_image = cv2.resize(deskewed_image, (new_width, new_height), interpolation=cv2.INTER_AREA)

    return resized_image

def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Main function
def main():
    image_path = '/Users/shashank/Downloads/picture.png'  # Update this path
    preprocessed_image = preprocess_image(image_path)
    text = extract_text(preprocessed_image)
    print("Extracted Text:")
    print(text)

if __name__ == "__main__":
    main()