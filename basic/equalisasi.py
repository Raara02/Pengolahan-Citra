import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca citra
citra = cv2.imread("ss1.jpg")

# Mengonversi citra ke dalam skala abu-abu
citra_gray = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)

# Melakukan equalisasi histogram
citra_equalized = cv2.equalizeHist(citra_gray)

# Menampilkan citra asli dan citra yang sudah di-equalisasi
plt.subplot(1, 2, 1)
plt.imshow(citra_gray, cmap='gray')
plt.title('Citra Gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(citra_equalized, cmap='gray')
plt.title('Citra Equalisasi')
plt.axis('off')

plt.show()
