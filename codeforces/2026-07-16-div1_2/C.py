for _ in range(int(input())):
    n, k = map(int, input().split())

    # Separate Case
    if n == 1:
        if k == 1:
            print("YES")
            print(0)
        else:
            print("NO")
        continue

    # As f(n - 1) = n
    # Therefore k becomes kdash = k ^ n
    kdash = k ^ n

    # bit length of kdash > bit length of (n - 1) 
    # then we can never xor the first (n - 1) numbers and achieve value kdash
    if kdash.bit_length() > (n - 1).bit_length():
        print("NO")
        continue

    s = list()

    # if kdash is less than or equal to (n - 1) then we keep the (n - 1)th element as kdash
    if 0 < kdash <= n - 1:
        s.append(kdash)
    # if kdash is greater than (n - 1) then we add 2 elements (n - 1) and (n - 1) ^ kdash
    # whose overall xor is just kdash
    elif kdash:
        s.append(n - 1)
        s.append((n - 1) ^ kdash)
    s.append(0)

    # Create Answer array
    ans = s[:]
    for i in range(n):
        if i not in s:
            ans.append(i)
    print("YES")
    # Reversing the array as that is the requirement
    print(*reversed(ans))