import cv2

#MEMBACA
citra = cv2.imread('ss1.jpg')

#MENAMPILKAN
cv2.imshow("Shizuka-biru", citra[:,:,0])
cv2.imshow("Shizuka-hijau", citra[:,:,1])
cv2.imshow("Shizuka-merah", citra[:,:,2])

# Menunggu Input dan Menutup Jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
