def maxPalindrome(i, j, n, a, temp, m):
    while i >= 0 and j < n:
        if a[i] == a[j]:
            temp[a[i]] = True
            i -= 1
            j += 1
        else:
            break
    
    for i in range(m):
        if not temp[i]:
            return i
    return m

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(pp) for pp in input().split()]
    # Case 1: expand first zero as center
    # Case 2: expand second zero as center
    maxAns = 1
    lZero = -1
    rZero = -1
    for i in range(2 * n):
        if a[i] == 0:
            # Case 1: expand first zero as center
            if lZero == -1:
                lZero = i
            # Case 2: expand second zero as center
            elif rZero == -1:
                rZero = i
            
            mexArray = [False] * (n + 1)
            maxLength = maxPalindrome(i, i, 2 * n, a, mexArray, n)
            maxAns = max(maxAns, maxLength)
    
    # Case 3: expand center of both zeros
    mexArray = [False] * (n + 1)
    if (rZero - lZero) % 2:
        midEle = (rZero + lZero) // 2
        maxLength = maxPalindrome(midEle, midEle + 1, 2 * n, a, mexArray, n)
    else:
        midEle = (rZero + lZero) // 2
        maxLength = maxPalindrome(midEle, midEle, 2 * n, a, mexArray, n)
    maxAns = max(maxLength, maxAns)
    print(maxAns)