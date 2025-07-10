import cv2

# Membaca citra
citra_asli = cv2.imread("ss1.jpg")

# Mengubah citra menjadi citra gray
citra_keabuan = cv2.cvtColor(citra_asli, cv2.COLOR_BGR2GRAY)

# Menerapkan ambang batas (threshold) pada citra gray
_, citra_biner = cv2.threshold(citra_keabuan, 127, 255, cv2.THRESH_BINARY)

# Menampilkan citra biner
cv2.imshow("Citra Biner", citra_biner)
cv2.imshow("Citra gray", citra_keabuan)
cv2.waitKey(0)
cv2.destroyAllWindows()