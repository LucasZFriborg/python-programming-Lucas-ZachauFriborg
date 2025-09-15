import math

# a)
a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(f'The hypothenuse is {c} length units.')

# b)
c = 7.0
a = 5.0
b = math.sqrt(c**2 - a**2)

print(f'The other cathetus is {round(b, 1)} length units.')

# 2. Classification accuracy
acc = 300/365

print(f'The accuracy is {acc:.2f} percent')

# 3. Classification accuracy
accuracy = (2 + 985) / (2 + 985 + 2 + 11)

print(f'Accuracy: {accuracy}')

# 4. Line
# Räta linjens ekvation => y = kx + m

A = (4, 4)
B = (0, 1)

k = (A[1] - B[1]) / (A[0] - B[0])
print(k)

# dont forget to compute m as well^

# 5. Euclidean distance
import math

P = (3, 5)
Q = (-2, 4)

p1 = 3
p2 = 5
q1 = -2
q2 = 4

d = math.sqrt((p1-q1)**2 + (p2 - q2)**2)
print(d)

# 6. Euclidean distance in 3D
import math

p1, p2, p3 = (2, 1, 4)
q1, q2, q3 = (3, 1, 0)

print(math.sqrt((p1-q1)**2 + (p2-q2) + (p3-q3)**2))
