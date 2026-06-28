t = int(input())
for _ in range(t):
    n = int(input())
    # Size of p is n - 1
    p  = [int(x) for x in input().split()]
    # [Depth, Parent]
    depthAndParent = [[0, 0]]
    for i in range(n - 1):
        parent = p[i]
        parentDepth = depthAndParent[parent - 1][0]
        depthAndParent.append([parentDepth + 1, parent])

    nary = {}
    for i in range(1, n):
        currDepth = depthAndParent[i][0]
        currParent = depthAndParent[i][1]
        if currDepth in nary:
            nary[currDepth].append(currParent)
        else:
            nary[currDepth] = [currParent]
    ans = n
    for i in nary.items():
        print("ITEM: ",i)
    for i, j in nary.items():
        
        uniques = 0
        sumOfUniques = ((uniques + 1) * uniques) // 2
        ans += sumOfUniques
    print("Answer: ", ans)
    # print(ans)