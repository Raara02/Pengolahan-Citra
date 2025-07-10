import cv2
from matplotlib import pyplot as plt

# Membaca citra
citra = cv2.imread("ss1.jpg")

# Menghitung histogram untuk setiap saluran warna
hist_blue = cv2.calcHist([citra], [0], None, [256], [0, 256])
hist_green = cv2.calcHist([citra], [1], None, [256], [0, 256])
hist_red = cv2.calcHist([citra], [2], None, [256], [0, 256])

# Menampilkan histogram untuk setiap saluran warna
plt.plot(hist_blue, color='blue', label='Blue')
plt.plot(hist_green, color='green', label='Green')
plt.plot(hist_red, color='red', label='Red')

plt.title('Histogram Citra')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')
plt.legend()
plt.show()