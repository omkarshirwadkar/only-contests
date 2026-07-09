# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(s) for s in input().split()]
    
    base, mx = 0, 1
    wait = [0]*n
    for i in range(n):
        mx = max(mx, a[i])
        wait[i] = mx - a[i]
        base += wait[i]
    
    
    mnch, mx = 0, 1
    for i in range(n):
        curch = - wait[i]
        curmx = mx
        if a[i] > mx:
            for j in range(i+1, n):
                if a[j] >= a[i]: break
                curmx = max(curmx, a[j])
                curch += curmx - a[j] - wait[j]
        mnch = min(mnch, curch)
        mx = max(mx, a[i])
    print(base + mnch)