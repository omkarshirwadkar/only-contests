t = int(input())
for _ in range(t):
    n = int(input())
    h = [int(pp) for pp in input().split()]
    print(1 + max(h) - min(h))