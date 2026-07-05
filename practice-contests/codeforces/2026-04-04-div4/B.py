t = int(input())
for _ in range(t):
    a = [int(pp) for pp in input().split()]
    suma = sum(a)
    maxAns = -67 * 8
    for i in a:
        maxAns = max(maxAns, -(suma - 2 * i))
    print(maxAns)