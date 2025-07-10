import cv2
import numpy as np

# Membaca citra
citra = cv2.imread('SS1.JPG', 0)

# Membuat kernel
kernel = np.ones((5, 5), np.uint8)

# Melakukan operasi erosi
erosi = cv2.erode(citra, kernel, iterations=1)
# Melakukan operasi dilasi
dilasi = cv2.dilate(citra, kernel, iterations=1)
# Melakukan operasi opening (erosi diikuti dilasi)
opening = cv2.morphologyEx(citra, cv2.MORPH_OPEN, kernel)
# Melakukan operasi closing (dilasi diikuti erosi)
closing = cv2.morphologyEx(citra, cv2.MORPH_CLOSE, kernel)

# Menampilkan citra asli, hasil erosi, hasil dilasi, hasil opening, dan hasil closing
cv2.imshow('Citra Asli', citra)
cv2.imshow('Hasil Erosi', erosi)
cv2.imshow('Hasil Dilasi', dilasi)
cv2.imshow('Hasil Opening', opening)
cv2.imshow('Hasil Closing', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
