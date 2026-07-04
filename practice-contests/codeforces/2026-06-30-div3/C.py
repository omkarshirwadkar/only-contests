t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    # if change count is 1 then only answer is 2 else it is 1
    change = True
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            # change will become False for the 1st time
            change = not change
            # if change is True then it means change has happened twice, 
            # so we break knowing the answer is 1
            if change:
                break
    if change:
        print(1)
    else:
        print(2)