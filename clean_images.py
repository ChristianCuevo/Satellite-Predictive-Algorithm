import rasterio
import os
import shutil

"""
clean_images.py

This script scans the xView2 dataset for corrupted or malformed .tif files,
removes them, and organizes valid images and labels into a cleaned structure.

Author: Christian 
Date: 2025-04-01
"""
input_base = "g:/Projects/Satelite-Predictive-Algorithim"  # base directory
output_base = "cleaned_data"

splits = ['Hold', 'Test', 'Tier1', 'Tier3']

# Function to validate image


def is_valid_tif(image_path):
    try:
        with rasterio.open(image_path) as src:
            return src.count >= 3  # (R, G, B)
    except:
        return False


for split in splits:
    input_img_dir = os.path.join(input_base, split, "images")
    input_lbl_dir = os.path.join(input_base, split, "labels")
    output_img_dir = os.path.join(output_base, split, "images")
    output_lbl_dir = os.path.join(output_base, split, "labels")

    os.makedirs(output_img_dir, exist_ok=True)
    os.makedirs(output_lbl_dir, exist_ok=True)

    for filename in os.listdir(input_img_dir):
        if filename.endswith(".tif"):
            image_path = os.path.join(input_img_dir, filename)
            label_path = os.path.join(
                input_lbl_dir, filename.replace(".tif", ".json"))

            if is_valid_tif(image_path):
                shutil.copy(image_path, output_img_dir)
                if os.path.exists(label_path):
                    shutil.copy(label_path, output_lbl_dir)
            else:
                print(f"Corrupt or incomplete: {filename}")
