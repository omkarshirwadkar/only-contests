t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    for i in range(n):
        curr = i + 1
        divi = (n // curr)
        ans += divi**2
    print(ans)