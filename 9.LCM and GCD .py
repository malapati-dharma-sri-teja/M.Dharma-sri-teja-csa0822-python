import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


gcd = math.gcd(a, b)

lcm = abs(a * b) 

print("GCD:", gcd)
print("LCM:", lcm)
