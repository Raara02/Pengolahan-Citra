import cv2
import numpy as np
from matplotlib import pyplot as plt
# Membaca citra
citra = cv2.imread('ss1.jpg')

# Membuat citra negatif
citra_negatif = 255 - citra

# Menampilkan citra asli dan citra negatif
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(citra, cv2.COLOR_BGR2RGB))
plt.title('Citra Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(citra_negatif, cv2.COLOR_BGR2RGB))
plt.title('Citra Negatif')
plt.axis('off')

plt.show()