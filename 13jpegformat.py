import cv2
import os

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")
qualities = [90, 70, 50, 30, 10]

print(f"{'Quality':<10} | {'File Name':<15} | {'Size (KB)':<10}")
print("-" * 42)

for q in qualities:
    fname = f"jpeg_q{q}.jpg"
    # JPEG quality parameter
    cv2.imwrite(fname, img, [cv2.IMWRITE_JPEG_QUALITY, q])
    size_kb = os.path.getsize(fname) / 1024
    print(f"{q:<10} | {fname:<15} | {size_kb:<10.2f}")
