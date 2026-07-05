t = int(input())
for _ in range(t):
    n = int(input())
    mul = 1
    a = [1]
    for i in range(n - 1):
        a.append(mul * (mul + 2))
        mul += 2
    print(*a)