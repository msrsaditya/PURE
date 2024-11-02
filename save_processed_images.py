def save_image(image, filename):
    """
    Save the processed image to a file.
    :param filename: The path where the image will be saved.
    """
    cv2.imwrite(filename, image)