def display_image(image, window_name='Image'):
    """
    Display an image in a window.
    :param window_name: The name of the window.
    """
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()