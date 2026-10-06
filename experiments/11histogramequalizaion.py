import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg", cv2.IMREAD_GRAYSCALE)

# Equalization
equ = cv2.equalizeHist(img)

# Plotting images and histograms
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Original Histogram')

plt.subplot(2, 2, 3)
plt.imshow(equ, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(equ.ravel(), 256, [0, 256])
plt.title('Equalized Histogram')

plt.tight_layout()
plt.show()
