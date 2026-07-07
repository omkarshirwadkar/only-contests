t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pp) for pp in input().split()]
    maxa = max(a)
    if maxa > 2:
        print("YES")
    elif maxa == 2:
        if a.count(maxa) > 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")