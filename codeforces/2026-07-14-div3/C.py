from math import gcd
t = int(input())
for _ in range(t):
    n, x, y = [int(s) for s in input().split()]
    p = [int(s) for s in input().split()]
    gcdXY = gcd(x, y)
    ans = True
    for i in range(n):
        diff = abs(p[i] - (i + 1))
        if diff % gcdXY:
            ans = False
            break
    if ans:
        print("YES")
    else:
        print("NO")