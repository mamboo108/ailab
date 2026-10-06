import cv2

img = cv2.imread(r"C:\Users\anton\Downloads\sanjuu.jpg")

# medianBlur takes an odd integer aperture linear size
m3 = cv2.medianBlur(img, 3)
m5 = cv2.medianBlur(img, 5)
m7 = cv2.medianBlur(img, 7)

cv2.imshow('Median 3x3', m3)
cv2.imshow('Median 5x5', m5)
cv2.imshow('Median 7x7', m7)
cv2.waitKey(0)
cv2.destroyAllWindows()
