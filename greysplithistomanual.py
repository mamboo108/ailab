import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = gray.shape

# Divide into 2 x 4 blocks
bh = h // 2
bw = w // 4

for i in range(2):
    for j in range(4):

        block = gray[i*bh:(i+1)*bh, j*bw:(j+1)*bw]

        # Manual histogram
        hist = [0] * 256

        for row in block:
            for pixel in row:
                hist[pixel] += 1

        plot_idx = i * 4 + j + 1
        plt.subplot(2, 4, plot_idx)
        plt.plot(hist) #this only also fine
        plt.title(f"Block ({i+1}, {j+1})")
        plt.xlim([0, 255])

plt.tight_layout()
plt.show()
