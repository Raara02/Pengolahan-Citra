import cv2
import numpy as np

# Membaca citra
citra = cv2.imread('ss1.jpg')

# Mengaplikasikan filter rata-rata
kernel = np.ones((5, 5), np.float32) / 25
citra_hasil = cv2.filter2D(citra, -1, kernel)

# Menampilkan citra asli dan citra hasil filtering
cv2.imshow('Citra Asli', citra)
cv2.imshow('Citra Hasil', citra_hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()
