import cv2
import os

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")
compressions = [0, 3, 5, 7, 9]

print(f"{'Comp Level':<12} | {'File Name':<15} | {'Size (KB)':<10}")
print("-" * 44)

for c in compressions:
    fname = f"png_c{c}.png"
    # PNG compression: 0 (fastest, largest) to 9 (slowest, smallest)
    cv2.imwrite(fname, img, [cv2.IMWRITE_PNG_COMPRESSION, c])
    size_kb = os.path.getsize(fname) / 1024
    print(f"{c:<12} | {fname:<15} | {size_kb:<10.2f}")
