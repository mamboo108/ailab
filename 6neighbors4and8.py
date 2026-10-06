import cv2
import numpy as np

# Read image as grayscale and binarize
img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg", cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
h, w = binary.shape

# Arrays to store neighbour counts for each pixel
count_4 = np.zeros((h, w), dtype=int)
count_8 = np.zeros((h, w), dtype=int)

# Direction offsets
# 4-Neighbours: Top, Bottom, Left, Right
d4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 8-Neighbours: All 8 directions
d8 = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

for r in range(h):
    for c in range(w):
        current_color = binary[r, c]

        # 4-Neighbours check
        for dr, dc in d4:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if binary[nr, nc] == current_color:
                    count_4[r, c] += 1

        # 8-Neighbours check
        for dr, dc in d8:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if binary[nr, nc] == current_color:
                    count_8[r, c] += 1

print("Sample 4-neighbour counts (top-left 5x5 block):\n", count_4[:5, :5])
print("Sample 8-neighbour counts (top-left 5x5 block):\n", count_8[:5, :5])
