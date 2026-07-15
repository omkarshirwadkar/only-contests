for _ in range(int(input())):
    n, p = map(int, input().split())
    s = input()
    # Object at position P wants to reach any end 0 or n + 1 in minimum change of Direction
    left = s[:p].count('R')
    right = s[p-1:].count('L')
    print(min(left, right))