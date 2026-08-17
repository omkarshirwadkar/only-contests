t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pj) for pj in input().split()]
    countConsecutives = []

    for i in range(1, n):
        print(i)