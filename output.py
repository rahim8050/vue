import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# this is an update 
# Load the images
image_paths = ["/home/rahim/Desktop/vue-only/messi.jpg"]
images = [cv2.imread(img_path) for img_path in image_paths]

# Convert images from BGR to RGB (for correct display in matplotlib)
images = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB) for img in images]

# Display the images before annotation
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
for ax, img, path in zip(axes, images, image_paths):
    ax.imshow(img)
    ax.set_title(f"Original Image: {path.split('/')[-1]}")
    ax.axis("off")

plt.show()