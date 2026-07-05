t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pp) for pp in input().split()]
    suffMin = [1000000] * n
    suffMin[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        suffMin[i] = min(suffMin[i + 1], a[i])
    ans = 0
    curr = suffMin[0]
    maxBlock = 1
    currBlock = 0
    for i in range(n):
        ans += a[i] - suffMin[i]
        if suffMin[i] == curr:
            currBlock += 1
        else:
            curr = suffMin[i]
            currBlock = 1
        maxBlock = max(maxBlock, currBlock)
    print(ans + maxBlock - 1)