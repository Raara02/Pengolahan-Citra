import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv2.imread("D:/semester3/PENGCIT/caisin.jpeg", 0) 

#Find edge with Canny edge detection
edges = cv2.Canny(img, 100, 200)

# Display
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Grayscale Image'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2), plt.imshow(edges, cmap='ocean')
plt.title('Edge Detection'), plt.xticks([]), plt.yticks([])

# Show the plot
plt.show()