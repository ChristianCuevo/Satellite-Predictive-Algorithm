import rasterio
import cv2
import numpy as np

# Resize and normalizes function this data is easier to work with


def load_and_preprocess_image(image_path, size=(256, 256)):
    """
    Loads a .tif image, selects RGB bands, resizes it, and normalizes pixel values.
    """
    with rasterio.open(image_path) as src:
        image = src.read([1, 2, 3])  # RGB bands
        image = np.transpose(image, (1, 2, 0))  # Convert from CHW to HWC

    image_resized = cv2.resize(image, size)
    image_normalized = image_resized.astype(np.float32) / 255.0
    return image_normalized
