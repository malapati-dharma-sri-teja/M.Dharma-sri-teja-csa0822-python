import math

print("=== Exchange Values ===")
a = 10
b = 20
print("Before exchange: a =", a, ", b =", b)
a, b = b, a
print("After exchange:  a =", a, ", b =", b)

print("\n=== Circulate Values ===")
x = 1
y = 2
z = 3
print("Before circulation: x =", x, ", y =", y, ", z =", z)
x, y, z = z, x, y
print("After circulation:  x =", x, ", y =", y, ", z =", z)

print("\n=== Distance Between Two Points ===")
x1, y1 = 3, 4
x2, y2 = 7, 1
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance between ({x1},{y1}) and ({x2},{y2}) is: {distance:.2f}")
