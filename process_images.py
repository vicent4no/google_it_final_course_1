from PIL import Image
import os
import sys

original_folder = input("Insert images folder path: ")
new_folder = input("Insert new folder to store processed images: ")

try:
    images_list = os.listdir(original_folder)

    # Creating path if it doesn't exists.
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    # Processing images and saving them in new folder.
    for unprocessed_image in images_list:
        with Image.open(f"{original_folder}/{unprocessed_image}") as image:
            image.rotate(-90).resize((128, 128)).save(f"{new_folder}/{unprocessed_image}")

    sys.exit(0)

except Exception as e:
    print(f"Something happened: {e}")
    sys.exit(1)


