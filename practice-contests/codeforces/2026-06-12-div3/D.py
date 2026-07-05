t = int(input())
for _ in range(t):
    n, k = [int(pp) for pp in input().split()]
    a = [int(pp) for pp in input().split()]
    # Sorting array so we can count frequency of max element
    a.sort(reverse=True)
    # If only one element present and length is odd
    if a[0] == a[-1] and n % 2:
        print("NO")
    # If only one element present and length is even
    elif a[0] == a[-1] and not n % 2:
        print("YES")
    else:
        i = 0
        ansFound = False
        while i < n:
            curr = a[i]
            cnt = 0
            # to get the count of the current maximum element
            while curr == a[i]:
                cnt += 1
                i += 1
            # If count is even then pick max element first
            if not cnt % 2:
                ansFound = True
                break
            # Index out of bound
            if i == n:
                break
            # count of max element is odd
            # if curr - a[i] <= k then we choose the a[i] first 
            # and in 2nd turn we choose max element
            if curr <= k + a[i]:
                ansFound = True
                break
        if ansFound:
            print("YES")
        else:
            print("NO")