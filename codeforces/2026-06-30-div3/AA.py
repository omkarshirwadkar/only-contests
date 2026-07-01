t = int(input())
for _ in range(t):
    x, y = [int(s) for s in input().split()]
    mod = x % y
    if not mod:
        print("YES")
    else:
        print("NO")