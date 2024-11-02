def extract_text(image, lang='eng'):
    """
    Extract text from the preprocessed image using Tesseract OCR with language support.
    :param lang: Language code(s) for Tesseract, e.g., 'eng' for English, 'spa' for Spanish, etc.
    """
    # Configure Tesseract for OCR with language support
    custom_config = f'--oem 3 --psm 6 -l {lang}'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text