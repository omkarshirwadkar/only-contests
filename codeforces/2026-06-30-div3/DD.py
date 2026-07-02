t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    b = [int(s) for s in input().split()]
    isPossible = True
    for i in range(n):
        if a[i] < b[i]:
            isPossible = False
            break
    if isPossible:
        print("YES")
    else:
        print("NO")