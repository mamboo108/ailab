# User coordinates
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Euclidean distance: sqrt((x2 - x1)^2 + (y2 - y1)^2)
euclidean_dist = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Manhattan distance: |x2 - x1| + |y2 - y1|
manhattan_dist = abs(x2 - x1) + abs(y2 - y1)

print(f"Point 1: ({x1}, {y1}), Point 2: ({x2}, {y2})")
print(f"Euclidean Distance: {euclidean_dist:.4f}")
print(f"Manhattan Distance: {manhattan_dist}")
