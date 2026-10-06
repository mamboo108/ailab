import cv2
import os

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")
qualities = [100, 70, 50, 30, 10]

print(f"{'WEBP Quality':<14} | {'File Name':<16} | {'Size (KB)':<10}")
print("-" * 46)

for q in qualities:
    fname = f"webp_q{q}.webp"
    # WEBP quality parameter (1 to 100)
    cv2.imwrite(fname, img, [cv2.IMWRITE_WEBP_QUALITY, q])
    size_kb = os.path.getsize(fname) / 1024
    print(f"{q:<14} | {fname:<16} | {size_kb:<10.2f}")
