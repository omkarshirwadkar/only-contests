# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    pref = [0] * n
    pref[0] = a[0]
    for i in range(1, n):
        pref[i] = max(pref[i - 1], a[i])
    # print(pref)
    ans = 0
    for i in range(n):
        ans += (pref[i] - a[i])
    print(ans)