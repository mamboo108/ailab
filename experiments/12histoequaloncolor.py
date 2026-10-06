import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")
# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Equalize only the V (Value / Brightness) channel
hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])

# Convert HSV back to BGR for OpenCV display / RGB for matplotlib
equalized_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# Convert for plotting in matplotlib
orig_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
equ_rgb = cv2.cvtColor(equalized_bgr, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(orig_rgb)
plt.title('Original Color Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Original Histogram')

plt.subplot(2, 2, 3)
plt.imshow(equ_rgb)
plt.title('Equalized Color Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.hist(equalized_bgr.ravel(), 256, [0, 256])
plt.title('Equalized Histogram')

plt.tight_layout()
plt.show()
