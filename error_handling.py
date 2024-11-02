import logging

# Configure logging
logging.basicConfig(filename='ocr_processing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def safe_extract_text(image, lang='eng'):
    """
    Safely extract text from the image with error handling.
    :param lang: Language code(s) for Tesseract.
    """
    try:
        text = extract_text(image, lang)
        logging.info("Text extraction successful.")
        return text
    except Exception as e:
        logging.error(f"Error during text extraction: {e}")
        return "Error during text extraction."

def main():
    image_path = 'path_to_your_image.png'  # Update this path
    try:
        preprocessed_image = preprocess_image(image_path)
        text = safe_extract_text(preprocessed_image)
        print("Extracted Text:")
        print(text)
    except Exception as e:
        logging.error(f"Error during processing: {e}")

if __name__ == "__main__":
    main()
