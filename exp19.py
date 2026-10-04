import cv2
import numpy as np

gray = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg", cv2.IMREAD_GRAYSCALE)

# cv2.Laplacian computes second derivatives.
# Use CV_64F to avoid clipping negative slope gradients, then take absolute value and convert to uint8.
lap3 = cv2.convertScaleAbs(cv2.Laplacian(gray, cv2.CV_64F, ksize=3))
lap5 = cv2.convertScaleAbs(cv2.Laplacian(gray, cv2.CV_64F, ksize=5))
lap7 = cv2.convertScaleAbs(cv2.Laplacian(gray, cv2.CV_64F, ksize=7))

cv2.imshow('Laplacian 3x3', lap3)
cv2.imshow('Laplacian 5x5', lap5)
cv2.imshow('Laplacian 7x7', lap7)
cv2.waitKey(0)
cv2.destroyAllWindows()
