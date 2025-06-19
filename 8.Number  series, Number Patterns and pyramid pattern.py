n = 10
rows = 5

print("Even numbers:")
for i in range(2, n+1, 2): print(i, end=' ')
print("\n")

print("Number pattern:")
for i in range(1, rows+1):
    print(*range(1, i+1))

print("\nPyramid pattern:")
for i in range(1, rows+1):
    print(' '*(rows-i) + '* '*i)
