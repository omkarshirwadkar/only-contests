t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    temp = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            temp += 1
    if temp == 1:
        print(2)
    else:
        print(1)