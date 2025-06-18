a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
temp = a
a = b
b = temp
print(f"\nAfter swapping with temporary variable: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping without temporary variable: a = {a}, b = {b}")
