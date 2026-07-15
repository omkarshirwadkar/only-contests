for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    ct1, ct2 = 0, 0
    # The goal is to minimize the cost to make the array 0,1,0,1,0,1... or 1,0,1,0,1,0...
    for i in range(n):
        if i%2 == a[i]%2: ct1 += 1
        else: ct2 += 1
    print(min(ct1, ct2))