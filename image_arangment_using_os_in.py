import os
import shutil

# Source and destination folders
source_folder = "/home/kazuaki"
destination_folder = "/home/kazuaki/Pictures/Screenshots"

# Make sure destination exists
os.makedirs(destination_folder, exist_ok=True)

# Supported image extensions
image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".bmp")

# Get all files from source folder
files = [f for f in os.listdir(source_folder) if f.lower().endswith(image_extensions)]

for file in files:
    source_path = os.path.join(source_folder, file)

    # Start numbering from 1 and find the next available filename
    counter = 1
    while True:
        new_name = f"{counter}.png"
        destination_path = os.path.join(destination_folder, new_name)
        if not os.path.exists(destination_path):
            break
        counter += 1

    # Copy instead of rename (to keep original safe in home)
    shutil.copy2(source_path, destination_path)
    print(f"Copied: {file} -> {new_name}")
