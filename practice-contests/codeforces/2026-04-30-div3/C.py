t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pp) for pp in input().split()]
    diviSix = []
    diviTwo = []
    diviThree = []
    nonDivi = []
    for i in a:
        if not i % 6:
            diviSix.append(i)
        elif not i % 3:
            diviThree.append(i)
        elif not i % 2:
            diviTwo.append(i)
        else:
            nonDivi.append(i)
    ans = diviSix + diviTwo + nonDivi + diviThree
    print(*ans)