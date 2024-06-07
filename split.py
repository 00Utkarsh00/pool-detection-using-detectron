import os
import random
import shutil

def split_data(images_folder, annotations_folder, output_folder):
    # Create train, val, and test folders in the output directory
    for split in ['train', 'val', 'test']:
        split_folder = os.path.join(output_folder, split)
        os.makedirs(os.path.join(split_folder, 'image'), exist_ok=True)
        os.makedirs(os.path.join(split_folder, 'annotation'), exist_ok=True)

    # Get the list of image files
    image_files = sorted([f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg'))])

    # Set the random seed for reproducibility
    random.seed(42)

    # Shuffle the list of image files
    random.shuffle(image_files)

    # Calculate the split sizes
    total_images = len(image_files)
    train_size = int(0.7 * total_images)
    val_size = int(0.2 * total_images)
    test_size = total_images - train_size - val_size

    # Split the data
    train_images = image_files[:train_size]
    val_images = image_files[train_size:train_size + val_size]
    test_images = image_files[train_size + val_size:]

    # Move images and corresponding annotations to their respective folders
    for split, image_list in zip(['train', 'val', 'test'], [train_images, val_images, test_images]):
        for image_file in image_list:
            image_path = os.path.join(images_folder, image_file)
            annotation_path = os.path.join(annotations_folder, image_file)

            # Move image
            shutil.copy(image_path, os.path.join(output_folder, split, 'image'))

            # Move annotation
            shutil.copy(annotation_path, os.path.join(output_folder, split, 'annotation'))

    print("Data split into train, val, and test sets with separate image and annotation folders.")

# Specify the paths to the images, annotations, and output folders
images_folder = r"S:\BH-DATASET\images"
annotations_folder = r"S:\BH-DATASET\annotations"
output_folder = r"S:\BH-DATASET\output"
# Call the function to split the data
split_data(images_folder, annotations_folder, output_folder)
