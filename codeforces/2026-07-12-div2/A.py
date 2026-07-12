t = int(input())
for _ in range(t):
    n = int(input())
    ans = [0] * n
    ans[-1] = 1
    for i in range(2, n + 1):
        ans[i - 2] = i
    print(*ans)