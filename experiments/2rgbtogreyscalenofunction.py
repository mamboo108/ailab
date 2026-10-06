import cv2
import numpy as np

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")
h, w, _ = img.shape

# Initialize empty 2D matrices
gray = np.zeros((h, w), dtype=np.uint8)
binary = np.zeros((h, w), dtype=np.uint8)

# OpenCV loads images as BGR: Blue=index 0, Green=index 1, Red=index 2
for i in range(h):
    for j in range(w):
        b, g, r = img[i, j]
        # Weighted average formula: 0.299*R + 0.587*G + 0.114*B
        val = int(0.299 * r + 0.587 * g + 0.114 * b)
        gray[i, j] = val
        binary[i, j] = 255 if val >= 127 else 0

cv2.imshow('Manual Gray', gray)
cv2.imshow('Manual Binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
