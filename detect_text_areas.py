def detect_text_areas(image):
    """
    Detect and draw bounding boxes around text areas in the image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 20:  # Filter out small areas
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image