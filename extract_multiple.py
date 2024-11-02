import os

def process_directory(directory_path):
    """
    Process all images in a directory and extract text from each.
    :param directory_path: The path to the directory containing images.
    """
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            image_path = os.path.join(directory_path, filename)
            print(f"Processing {filename}")
            preprocessed_image = preprocess_image(image_path)
            text = extract_text(preprocessed_image)
            print(f"Text from {filename}:")
            print(text)
            print("\n---\n")

# Example usage
process_directory('/Users/shashank/Downloads')