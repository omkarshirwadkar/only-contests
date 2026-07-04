t = int(input())
for _ in range(t):
    a, b, x = [int(pp) for pp in input().split()]
    ans = float("inf")
    i = 0
    while a != b:
        if b > a:
            a, b = b, a
        ans = min(ans, i + a - b)
        a = a // x
        i += 1
    ans = min(ans, i)
    print(ans)