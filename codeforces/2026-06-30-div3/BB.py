def isGood(n):
    s = str(n)
    setS = set()
    for i in s:
        setS.add(i)
        if len(setS) > 2:
            break
    return len(setS) <= 2

arr = []
for i in range(2, 200001):
    if isGood(i):
        arr.append(i)

t = int(input())
for _ in range(t):
    x = int(input())
    found = False
    ans = -1
    for i in arr:
        if isGood(i * x):
            ans = i
            found = True
            break
    if not found:
        print(2)
    else:
        print(ans)