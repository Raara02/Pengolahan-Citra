import cv2
import numpy as np #untuk perhitungan matematis

#MEMBACA
citra = cv2.imread("ss1.jpg")

#membaca warna bgr dan simpan dgn variabel terpisah 
b = citra[:,:,0]
g = citra[:,:,1]
r = citra[:,:,2]

#menyimpan jumlah baris dan kolom dari citra
jum_baris = len(citra)
jum_kolom = len(citra[0])

#menyimpan citra baru dengan nilai 0 
citra_gray = np.zeros((jum_baris, jum_kolom))

#menghituung nilai piksel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom): #ada brp kolom pada 0
        citra_gray[i, j] = round (0.299 * r[i, j] + 0.587 * g[i, j] + 0.14 * b[i, j])

#mengubah nilai integer menjadi unsigned integer
citra_gray = citra_gray.astype(np.uint8)
print(citra)

cv2.imshow("Laura warna gray", citra_gray)
cv2.waitKey()