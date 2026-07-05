t = int(input())
for _ in range(t):
    n = int(input())
    # a = [int(pp) for pp in input().split()]
    s = input()
    openBracket = s.count("(")
    closeBracket = n - openBracket
    if openBracket == closeBracket:
        print("YES")
    else:
        print("NO")