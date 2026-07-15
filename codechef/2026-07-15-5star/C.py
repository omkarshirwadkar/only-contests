for _ in range(int(input())):
    n = int(input())
    s = list(input())
    # "z" is flipped to "a" and make it lexicographically smallest, 
    # so make the 1st group of "z" as "a"
    for i in range(n):
        if s[i] != 'z': continue
        for j in range(i, n):
            if s[j] == 'z':
                s[j] = 'a'
            else:
                break
        break
    print(''.join(s))