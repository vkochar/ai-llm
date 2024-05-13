from PIL import Image
import os

# Specify the input directory containing your images
input_directory = '../data/car'

# Set the target size (500x500 pixels)
target_size = (500, 500)

def resize_images():
    for filename in os.listdir(input_directory):
        try:
            if filename.lower().endswith(('.jpg', '.png')):
                image_path = os.path.join(input_directory, filename)
                img = Image.open(image_path)
                resized_img = img.resize(target_size)
                resized_img.save(os.path.join(input_directory, f"resized/{filename}"), 'JPEG', optimize=False)
        except Exception as e:
            print(e)

resize_images()