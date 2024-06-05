import cv2
import numpy as np

# Membaca gambar
image = cv2.imread('daun.png', cv2.IMREAD_GRAYSCALE)

# Menentukan threshold menggunakan metode Otsu
_, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Inversi threshold
thresh = cv2.bitwise_not(thresh)

# Menampilkan hasil
cv2.imshow('Segmented Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
