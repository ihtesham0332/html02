import os
import shutil

def rename_images(folder_path):
    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter only image files (you can adjust the extensions as needed)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # If no image files are found, print a message and return
    if not image_files:
        print(f"No image files found in: {folder_path}")
        return

    # Create a directory to store the renamed images
    output_folder = os.path.join(folder_path, 'renamed_images')
    os.makedirs(output_folder, exist_ok=True)

    # Rename and move each image
    for index, image_file in enumerate(image_files, start=1):
        old_path = os.path.join(folder_path, image_file)
        new_name = f'image_{index:03d}'  # This will generate names like image_001, image_002, etc.
        new_path = os.path.join(output_folder, new_name + os.path.splitext(image_file)[1])

        shutil.copy(old_path, new_path)
        print(f"Renamed {image_file} to {new_name}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing images: ")
    rename_images(folder_path)
