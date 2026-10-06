import cv2
import numpy as np

gray = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg", cv2.IMREAD_GRAYSCALE)

# Formula: s = c * log(1 + r)
# c = 255 / log(1 + max(r))
c = 255 / np.log(1 + float(np.max(gray)))
log_transformed = c * np.log(1 + gray.astype(np.float64))

# Convert back to uint8
log_transformed = np.array(log_transformed, dtype=np.uint8)

cv2.imshow('Original Grayscale', gray)
cv2.imshow('Log Transform', log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
