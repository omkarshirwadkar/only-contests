t = int(input())
for _ in range(t):
    n = int(input())
    # a = [int(pp) for pp in input().split()]
    m = 3 * n
    a = [0] * (m)
    for i in range(n):
        idx = 3 * i
        a[idx] = i + 1
        a[idx + 2] = m - 2 * i
        a[idx + 1] = m - 1 - 2 * i
    print(*a)