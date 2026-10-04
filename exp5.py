import cv2
import numpy as np

# Create two sample binary images of size 200x200
img1 = cv2.imread(r"C:\Users\anton\Downloads\rect.jpeg")
img2 = cv2.imread(r"C:\Users\anton\Downloads\circ.jpeg")

# Bitwise Operations
bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)

cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('AND', bit_and)
cv2.imshow('OR', bit_or)
cv2.imshow('XOR', bit_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()
