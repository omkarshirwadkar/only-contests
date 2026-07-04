t = int(input())
for _ in range(t):
    n, k = [int(pp) for pp in input().split()]
    sa = list(input())
    for i in range(n - k):
        if sa[i] == "1":
            sa[i] = "0"
            if sa[i + k] == "1":
                sa[i + k] = "0"
            else:
                sa[i + k] = "1"
    ss = ["0" for i in range(n)]
    if sa == ss:
        print("YES")
    else:
        print("NO")