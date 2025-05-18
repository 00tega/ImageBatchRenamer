# ImageBatchRenamer
ImageBatchRenamer is a lightweight Python script that recursively renames image files in a folder and its subfolders using a consistent naming format. It supports multiple image formats and organizes file names based on numerical order found in the original names. Ideal for organizing scraped images, datasets, or personal photo collections.

A simple Python script to batch rename image files in a folder and all its subfolders. It renames each image file using a customizable base name followed by an incrementing number, preserving the original file extensions.

# Features

- Supports common image formats: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- Recursively scans through all subfolders
- Avoids overwriting by skipping already-existing renamed files
- Sorts images by the first number found in their filenames
- Easy to customize with your own folder path and base name

# How It Works

The script:
1. Walks through all subdirectories of a specified root folder
2. Collects image files with supported extensions
3. Sorts them based on the first number found in the filename
4. Renames them in the format: `base_name_1.ext`, `base_name_2.ext`, etc.

# Usage

1. Edit the `folder_path` variable at the bottom of the script with your path.
2. (Optional) Change the `base_name` argument if you want a different prefix.
3. Run the script using Python:

```bash
python ImageBatchRenamer.py
