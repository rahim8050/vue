# Cell 1: Imports
import numpy as np
import cv2
from matplotlib import pyplot as plt
# %matplotlib inline

# Cell 2: Load and Check Image
try:
    img = cv2.imread('/home/rahim/Desktop/vue-only/messi.jpg')
    if img is not None:
        print("Image loaded successfully!")
        print("Shape:", img.shape)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()
    else:
        print("Error: Image not found or invalid format.")
except Exception as e:
    print(f"An error occurred: {str(e)}")