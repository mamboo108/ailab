import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define Normalized Box Kernels
k3 = np.ones((3, 3), dtype=np.float32) / 9.0
k5 = np.ones((5, 5), dtype=np.float32) / 25.0
k7 = np.ones((7, 7), dtype=np.float32) / 49.0

# Apply cv2.filter2D()
avg3 = cv2.filter2D(img_rgb, -1, k3)
avg5 = cv2.filter2D(img_rgb, -1, k5)
avg7 = cv2.filter2D(img_rgb, -1, k7)

# Display in 2x2 Plot
titles = ['Original', 'Averaging 3x3', 'Averaging 5x5', 'Averaging 7x7']
images = [img_rgb, avg3, avg5, avg7]

plt.figure(figsize=(8, 8))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
