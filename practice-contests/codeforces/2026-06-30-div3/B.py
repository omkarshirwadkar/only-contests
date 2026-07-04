t = int(input())
for _ in range(t):
    x = int(input())
    # a = [int(pp) for pp in input().split()]
    xStr = str(x)
    y = 10 ** (len(xStr)) + 1
    print(y)