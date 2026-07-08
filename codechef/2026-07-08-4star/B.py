# cook your dish here
t = int(input())
for _ in range(t):
    # n = int(input())
    x, y = [int(s) for s in input().split()]
    print(x + max(0, y - x) // 2)