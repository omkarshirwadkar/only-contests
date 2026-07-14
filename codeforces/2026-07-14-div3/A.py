t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    maxG = 0
    currG = 0
    for i in s:
        if i == "#":
            currG += 1
        else:
            currG = 0
        maxG = max(maxG, currG)
    print((maxG + 1) // 2)