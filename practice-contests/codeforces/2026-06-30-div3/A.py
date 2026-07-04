t = int(input())
for _ in range(t):
    x, y = [int(s) for s in input().split()]
    if x % y:
        print("NO")
    else:
        print("YES")