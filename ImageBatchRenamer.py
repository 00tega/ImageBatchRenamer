import os
import re

def extract_number(name):
    match = re.search(r'(\d+)', name)
    return int(match.group(1)) if match else float('inf')

def rename_images_in_subfolders(root_folder, base_name="dl"):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    images_list = []

    # Gather all images in subfolders (and root folder)
    for dirpath, _, filenames in os.walk(root_folder):
        for file in filenames:
            ext = os.path.splitext(file)[1].lower()
            if ext in valid_extensions:
                full_path = os.path.join(dirpath, file)
                images_list.append((file, full_path, dirpath))

    if not images_list:
        print("No images found in the folder or subfolders!")
        return

    # Sort by the number found in the filename
    images_list.sort(key=lambda x: extract_number(x[0]))

    count = 1
    for original_name, full_path, folder in images_list:
        ext = os.path.splitext(original_name)[1].lower()
        new_name = f"{base_name}_{count}{ext}"
        new_path = os.path.join(folder, new_name)

        # Check if new_path exists to avoid overwriting
        if os.path.exists(new_path):
            print(f"Skipping {new_name}, file already exists!")
            count += 1
            continue

        try:
            os.rename(full_path, new_path)
            print(f"Renamed: {original_name} → {new_name}")
        except Exception as e:
            print(f"Failed to rename {original_name}: {e}")
        count += 1

# Your root folder path here
folder_path = input("Enter the full path to the root folder: ")

rename_images_in_subfolders(folder_path)
