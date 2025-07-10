import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv2.imread('D:\SEMESTER3\PENGCIT\PENGOLAHAN CITRA\caisin.jpeg', 0) 

# Calculate gradients using Sobel operator
gradient_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Calculate magnitude of the gradient
magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# Calculate the angle (direction) of the gradient
angle = np.arctan2(gradient_y, gradient_x)

# Find edge with Canny edge detection
edges = cv2.Canny(img, 100, 200)

# Display
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Grayscale Image'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 2), plt.imshow(magnitude, cmap='hot')
plt.title('Gradient Magnitude'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 3, 3), plt.imshow(edges, cmap='ocean')
plt.title('Edge Detection'), plt.xticks([]), plt.yticks([])

# Show the plot
plt.show()
