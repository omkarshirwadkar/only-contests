t = int(input())
for _ in range(t):
    # n = int(input())
    x, y = [int(pp) for pp in input().split()]
    if x % 2 and y % 2:
        print("NO")
    else:
        print("YES")