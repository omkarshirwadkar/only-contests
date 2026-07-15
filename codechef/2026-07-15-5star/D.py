for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input()
    zero, one = a.count('0'), a.count('1')

    # case 1: Nothing can be done
    if min(zero, one) < k:
        print(a)
    # case 2: only 1 operation possible to take compliment, take min of original and compliment
    elif n == 2*k:
        flipped = ''.join('1' if x == '0' else '0' for x in a)
        print(min(a, flipped))
    # case 3: all zeros can be brought to the left to make it lexicographically smallest
    else:
        print('0'*zero + '1'*one)