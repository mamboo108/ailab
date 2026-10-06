import cv2
import numpy as np

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")
h, w = img.shape[:2]

# Take parameters as user input
tx = float(input("Enter X translation (pixels): "))
ty = float(input("Enter Y translation (pixels): "))
scale = float(input("Enter scaling factor (e.g., 0.5 or 1.5): "))
angle = float(input("Enter rotation angle (degrees): "))

# 1. Translation Matrix [[1, 0, tx], [0, 1, ty]]
M_trans = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(img, M_trans, (w, h))

# 2. Scaling
scaled = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)

# 3. Rotation around center
center = (w // 2, h // 2)
M_rot = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(img, M_rot, (w, h))

cv2.imshow('Translated', translated)
cv2.imshow('Scaled', scaled)
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
