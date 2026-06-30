t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    first = s[0]
    last = s[-1]
    if first == last:
        print(1)
    else:
        fc = s.count(first)
        lc = s.count(last)
        if fc == 1 or lc == 1:
            print(2)
        else:
            print(1)