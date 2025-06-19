def climb_stairs(n):
    if n <= 1:
        return 1
    a, b = 1, 1  # ways(0), ways(1)
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
n = 4
print("Output:", climb_stairs(n))
