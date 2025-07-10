import cv2
import numpy as np

# Membaca citra pertama
citra1 = cv2.imread('ss1.jpg')

# Membaca citra kedua
citra2 = cv2.imread('kaca.jpg')

# Mengubah ukuran kedua citra
citra2 = cv2.resize(citra2, (citra1.shape[1], citra1.shape[0]))

# Menambahkan kedua citra
tambah = cv2.add(citra1, citra2)
#kurang
kurang = cv2.subtract(citra1, citra2)
#bagi
bagi = cv2.divide(citra1, citra2)
#kali
perkalian = hasil_perkalian = cv2.multiply(citra1, citra2)

# Menampilkan citra hasil penjumlahan
cv2.imshow('Citra Penambahan', tambah)
cv2.imshow('Hasil Pengurangan', kurang)
cv2.imshow('Hasil Pembagian', bagi)
cv2.imshow('Hasil Perkalian', perkalian)

cv2.waitKey(0)
cv2.destroyAllWindows()
