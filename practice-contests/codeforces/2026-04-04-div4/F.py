t = int(input())
for _ in range(t):
    x, y = [int(s) for s in input().split()]
    if x > y or (x == 0 and not y % 2):
        print("NO")
    else:
        print("YES")
        n = x + y
        arr = []
        cnt = 0
        if n % 2:
            for i in range(2, y + 1):
                print(1, i)
                arr.append(i)
            for i in range(y + 1, n + 1):
                print(arr[cnt], i)
                cnt += 1
        else:
            for i in range(2, y + 2):
                print(1, i)
                arr.append(i)
            for i in range(y + 2, n + 1):
                print(arr[cnt], i)
                cnt += 1
            