import os
import sys
import re
from PIL import Image

def get_natural_sort_key(filename):

    """

    Extract numbers from a filename to sort t2.png' before '10.png'.

    """

    # Find all number groups in the filename
    return[int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)',filename)]

def create_pdf_from_images():
    try:
        # 1. ROBUST FOLDER DETECTION
        # This ensures we get the folder where the .py file actually sites regardless of where you run the command from.
        if getattr(sys, 'frozen', False):
            # If compiled as an executable
            current_folder = os.path.dirname(sys.executable)
        else:
            # If run as a script
            current_folder = os.path.dirname(os.path.abspath(__file__))

        print(f"Target folder: {current_folder}")

        # Use the folder name for the PDF name
        folder_name = os.path.basename(current_folder)

        # 2. Check the directory content (.jpg, .jpeg, .png, .tiff, .bmp)
        valid_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp')
        all_files = os.listdir(current_folder)
        files = [f for f in all_files if f.lower().endswith(valid_extensions)]

        # 3. Sort files based on the numbers in their names
        # This Handles 1.png, 2.png, 10.png correctly
        files.sort(key=get_natural_sort_key)

        if not files:
            print("No images found in this folder! Make sure your images end with .jpg, .png, etc.")
            return
        print(f"Found {len(files)} images. Preparing to merge...")
        # List to hold the image objects
        image_list = []

        # 4. Process the first image separately (it will be the base of the PDF)
        first_image_path = os.path.join(current_folder, files[0])
        first_image = Image.open(first_image_path)

        # Convert to RPG is necessary because PDF doesn't support transparency (Alpha channel)
        # The same way PNG doesn't, and it prevents errors.
        first_image = first_image.convert('RGB')

        for filename in files[1:]:
            img_path = os.path.join(current_folder, filename)
            img = Image.open(img_path)
            image_list.append(img.convert('RGB'))

        # 5. Save the result
        output_filename = f"{folder_name}.pdf"
        print(f"Saving {output_filename}...")

        first_image.save(
            output_filename,
            save_all=True,
            append_images=image_list
        )

        print("\nSUCCESS! PDF created successfully.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    create_pdf_from_images()
    input("\nPress Enter to exit") # To prevent the app from closing fast