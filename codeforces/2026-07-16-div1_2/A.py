for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    # Answer not possible
    if k * 2 > n:
        print(-1)
        continue
    ans = 0
    for i in range(k):
        # Count L's in the first k characters and R's in the last K characters
        ans += int(s[i] == 'L') + int(s[n - i - 1] == 'R')
    print(ans)