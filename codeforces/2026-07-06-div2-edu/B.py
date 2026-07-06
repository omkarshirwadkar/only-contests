t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pp) for pp in input().split()]
    oneCount = 0
    othCount = 0
    i = 0
    while i < n - 1:
        curr = a[i]
        if curr == 1:
            oneCount += 1
        else:
            othCount += 1
        if oneCount == othCount:
            i += 1
            break
        if oneCount > othCount:
            if a[i + 1] == 3:
                i += 1
            i += 1
            break
        i += 1
    if oneCount < othCount:
        print("NO")
        continue
    l2Count = 0
    thrCount = 0
    while i < n - 1:
        curr = a[i]
        if curr == 3:
            thrCount += 1
        else:
            l2Count += 1
        if l2Count >= thrCount:
            break
        i += 1
    if l2Count >= thrCount and l2Count:
        print("YES")
    else:
        print("NO")