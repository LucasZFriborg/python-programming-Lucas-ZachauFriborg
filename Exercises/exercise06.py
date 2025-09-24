# 1. Area
def area(base, height):
    return (base * height) / 2

print(f'Area of the triangle: {area(5, 4)}')

# 2. Euclidean distance
import math

# a)
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# b)
p1 = int(input('Enter p1: '))
q1 = int(input('Enter q1: '))
p2 = int(input('Enter p2: '))
q2 = int(input('Enter q2: '))

# c)
dist = euclidean_distance((p1, q1), (p2, q2))
print("Distance between the points:", dist)

points = [(10, 3), (-1, -9), (10, -10), (4, -2), (9, -10)]
origin = (0, 0)

print("\nDistance from origo to the points:")
for p in points:
    d = euclidean_distance(origin, p)
    print(f'Distance to point {p}: {d}')