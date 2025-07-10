import cv2
import numpy as np

# Membaca citra pertama
citra1 = cv2.imread('ss1.jpg')
# Membaca citra kedua
citra2 = cv2.imread('kaca.jpg')

# Mengubah ukuran kedua citra
citra2 = cv2.resize(citra2, (citra1.shape[1], citra1.shape[0]))

# Melakukan operasi AND pada kedua citra
citra_and = cv2.bitwise_and(citra1, citra2)
# Melakukan operasi OR pada kedua citra
citra_or = cv2.bitwise_or(citra1, citra2)
# Melakukan operasi XOR pada kedua citra
citra_xor = cv2.bitwise_xor(citra1, citra2)
# Melakukan operasi NOT pada citra pertama
citra_not = cv2.bitwise_not(citra1)

# Menampilkan citra hasil operasi
cv2.imshow('Hasil AND', citra_and)
cv2.imshow('Hasil OR', citra_or)
cv2.imshow('Hasil XOR', citra_xor)
cv2.imshow('Hasil NOT', citra_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
