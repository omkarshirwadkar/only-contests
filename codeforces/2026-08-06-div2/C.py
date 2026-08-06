import heapq
t = int(input())
for _ in range(t):
    n, m = [int(s) for s in input().split()]
    v = [int(s) for s in input().split()]
    a = []
    minArray = []
    ans = m
    for i in range(n):
        r = [int(s) for s in input().split()]
        minArray.append(min(r))
        a.append(r)
    temp = 0
    t1 = sorted(a[-1], reverse=True)
    for k in range(ans):
        v[-1] -= a[-1][k]
        if v[-1] <= 0:
            ans = k + 1
            break
    numbers = a[-1]
    heapq.heapify(numbers)
    for i in range(n - 2, -1, -1):
        for j in range(m):
            heapq.heappush(numbers, a[i][j])
        largest_ans = heapq.nlargest(ans, numbers)
        temp = 0
        for k in range(ans):
            v[i] -= largest_ans[k]
            if v[i] <= 0:
                ans = k + 1
                break
    print(ans)