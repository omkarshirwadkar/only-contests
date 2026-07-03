t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    b = [int(s) for s in input().split()]
    isPossible = True
    diffSum = 0
    for i in range(n):
        diffSum += a[i] - b[i]
        if diffSum > 0:
            isPossible = False
            break
    if isPossible:
        print("YES")
    else:
        print("NO")