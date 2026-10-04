import cv2

# Read image
img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")
h, w, c = img.shape
print(f"Height: {h}, Width: {w}, Channels: {c}")

# Convert BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert Grayscale to Binary using cv2.threshold (threshold=127, max_val=255)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display images
cv2.imshow('Original', img)
cv2.imshow('Grayscale', gray)
cv2.imshow('Binary', binary)

# Save images
cv2.imwrite('gray_output.jpg', gray)
cv2.imwrite('binary_output.jpg', binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
