import cv2

# Load image in color and convert to gray & binary
color_img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu2.jpg")
gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
_, bin_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

# Negative transformation: s = 255 - r
neg_bin = 255 - bin_img
neg_gray = 255 - gray_img
neg_color = 255 - color_img  # Performs element-wise inversion on all channels

cv2.imshow('Binary Negative', neg_bin)
cv2.imshow('Gray Negative', neg_gray)
cv2.imshow('Color Negative', neg_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
