t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2:
        print(-1)
    elif n == 1:
        print(1)
    else:
        ans = [1, 2, 3]
        remaining = n - 3
        for i in range(remaining):
            temp = ans[-1]
            ans.append(temp * 2)
        print(*ans)