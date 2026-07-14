t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    suma = 0
    sumn = 0
    isPoss = True
    for i in range(n):
        suma += a[i]
        sumn += (i + 1)
        if sumn > suma:
            isPoss = False
            break
    if isPoss:
        print("YES")
    else:
        print("NO")