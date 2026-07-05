t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pp) for pp in input().split()]
    maxAns = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            maxAns = max(maxAns, a[i] ^ a[j])
    print(maxAns)