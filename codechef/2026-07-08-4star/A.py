# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    mina = min(a)
    # print(mina)
    for i in range(n - 1):
        mini = min(a[i], a[i + 1])
        mina = max(mini, mina)
    print(mina)