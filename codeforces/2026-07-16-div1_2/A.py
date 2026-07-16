for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input()
    if n == 1:
        print(-1)
    elif n == 2:
        if a == "LL" or a == "RR" :
            print(1)
        elif a == "LR":
            print(2)
        else:
            print(0)
    else:
        a = list(a)
        mid = n // 2
        if k > mid:
            print(-1)
        elif k*2 == n:
            ans = 0
            for i in range(mid):
                if a[i] == "L":
                    ans += 1
            for i in range(mid, n):
                if a[i] == "R":
                    ans += 1
            print(ans)
        else:
            lCount = a.count("L")
            if not lCount:
                print(k)
            else:
                rC = 0
                ans = 0
                for i in range(n):
                    if rC >= k:
                        break
                    if a[i] == "R":
                        rC += 1
                    else:
                        a[i] = "R"
                        rC += 1
                        ans += 1
                lc = 0
                for i in range(n - 1, -1, -1):
                    if lc >= k:
                        break
                    if a[i] == "L":
                        lc += 1
                    else:
                        a[i] = "L"
                        lc += 1
                        ans += 1
                print(ans)