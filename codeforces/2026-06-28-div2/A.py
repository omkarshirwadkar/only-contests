t = int(input())
for _ in range(t):
    n, c = [int(x) for x in input().split()]
    a  = [int(x) for x in input().split()]
    b  = [int(x) for x in input().split()]
    sortedA = sorted(a)
    sortedB = sorted(b)
    isPossible = True
    for i in range(n):
        if sortedA[i] < sortedB[i]:
            isPossible = False
            break
    if not isPossible:
        print(-1)
    else:
        isReorderNeeded = False
        for i in range(n):
            if a[i] < b[i]:
                isReorderNeeded = True
                break
        if isReorderNeeded:
            totalOps = c
            for i in range(n):
                totalOps += (sortedA[i] - sortedB[i])
            print(totalOps)
        else:
            currOps = 0
            for i in range(n):
                currOps += (a[i] - b[i])
            totalOps = c
            for i in range(n):
                totalOps += (sortedA[i] - sortedB[i])
            print(min(totalOps, currOps))