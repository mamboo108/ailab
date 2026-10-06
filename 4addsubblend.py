import cv2

img1 = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")
img2 = cv2.imread(r"C:\Users\anton\Downloads\sanjuu2.jpg")

# Resize img2 to match img1 dimensions
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Addition and Subtraction
added = cv2.add(img1, img2)
subtracted = cv2.subtract(img1, img2)

# Blending: 0.7 * img1 + 0.3 * img2 + 0
blended = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('Added', added)
cv2.imshow('Subtracted', subtracted)
cv2.imshow('Blended', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
