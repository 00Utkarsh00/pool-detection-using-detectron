from PIL import Image
import os

def convert_jpg_to_png_and_delete(input_folder):
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            jpg_path = os.path.join(input_folder, filename)
            png_path = os.path.join(input_folder, os.path.splitext(filename)[0] + '.png')

            try:
                # Open the JPG image
                img = Image.open(jpg_path)

                # Save as PNG
                img.save(png_path, "PNG")

                print(f"Conversion successful: {jpg_path} -> {png_path}")

                # Delete the original JPG file
                os.remove(jpg_path)

                print(f"Deleted: {jpg_path}")

            except Exception as e:
                print(f"Conversion failed for {jpg_path}: {e}")

# Example usage
folders = ["images"]

for folder in folders:
    folder_path = os.path.join("S:/BH-DATASET", folder)
    convert_jpg_to_png_and_delete(folder_path)
