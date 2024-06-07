import os

def rename_files(folder_path):
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Sort the files based on their names
    files.sort(key=lambda x: int(x.split('.')[0]))

    # Initialize a counter for renaming
    counter = 160

    # Loop through each file in the folder
    for file_name in files:
        # Check if the file is a PNG or JPG file
        if file_name.lower().endswith(('.png', '.jpg')):
            # Construct the new file name
            new_name = f"{counter}.png"  # You can change the extension if needed

            # Construct the full paths for the old and new file names
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(old_path, new_path)

            # Increment the counter
            counter += 1

    print("Files renamed successfully.")

# Specify the folder path containing the PNG and JPG files
folder_path = r"S:\BH-DATASET\BH-POOLS\REGION_2\ANNOTATION_COLOR"
folder_path1 = r"S:\BH-DATASET\BH-POOLS\REGION_2\images"

# Call the function to rename files in the specified folder
rename_files(folder_path)
rename_files(folder_path1)
