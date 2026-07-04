t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pp) for pp in input().split()]
    b = [int(pp) for pp in input().split()]
    # In one operation we can add to the total sum of a if l == r
    # Else the total sum of a can be kept constant by taking even sized arrays
    # Observation: Prefix sum of a should always be smaller than that of b
    diffAB = 0
    isPossible = True
    for i in range(n):
        diffAB += a[i] - b[i]
        # checking the difference between prefixSum of a and b
        if diffAB > 0:
            isPossible = False
            break
    if isPossible:
        print("YES")
    else:
        print("NO")