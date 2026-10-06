import cv2
import numpy as np

def apply_gamma(image, gamma):
    # Normalize to [0, 1], raise to power gamma, scale back to [0, 255]
    inv_gamma = gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in range(256)]).astype(np.uint8)
    return cv2.LUT(image, table)

img_color = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

gamma_values = [0.2, 0.5, 1.5, 2.0, 3.0]

for g in gamma_values:
    res_gray = apply_gamma(img_gray, g)
    res_color = apply_gamma(img_color, g)
    cv2.imshow(f'Gray Gamma {g}', res_gray)
    cv2.imshow(f'Color Gamma {g}', res_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
