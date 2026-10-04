import cv2

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu2.jpg")

# GaussianBlur(source, (kernel_width, kernel_height), sigmaX)
g3 = cv2.GaussianBlur(img, (3, 3), 0)
g5 = cv2.GaussianBlur(img, (5, 5), 0)
g7 = cv2.GaussianBlur(img, (7, 7), 0)

cv2.imshow('Gaussian 3x3', g3)
cv2.imshow('Gaussian 5x5', g5)
cv2.imshow('Gaussian 7x7', g7)
cv2.waitKey(0)
cv2.destroyAllWindows()
