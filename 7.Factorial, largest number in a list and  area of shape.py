import math

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def largest(lst):
    return max(lst)

def area(shape, *args):
    if shape == "circle":
        return math.pi * args[0]**2
    elif shape == "rectangle":
        return args[0] * args[1]
    elif shape == "triangle":
        return 0.5 * args[0] * args[1]

print("Factorial of 5:", factorial(5))
print("Largest in [4, 9, 2, 7]:", largest([4, 9, 2, 7]))
print("Area of circle (r=3):", area("circle", 3))
print("Area of rectangle (3x4):", area("rectangle", 3, 4))
print("Area of triangle (base=5, height=2):", area("triangle", 5, 2))
