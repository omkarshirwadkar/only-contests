def minOperations(s1, s2):
    # convert binary string s1 to s2 in minimum operations
    # You can do the following operations each cost 1 unit
    # 1. Convert a single "0" to "1"
    # 2. Convert "11" to "00"
    if s1 == "1" and s2 == "0":
        return -1
    ls1, ls2 = list(s1), list(s2)
    n = len(s1)
    ops = 0
    for i in range(n):
        if ls1 != ls2:
            ops += 1
            if ls1 == "1":
                if i == n - 1:
                    ops += 1
                else:
                    ops += ls1[i + 1] == "0"
                    ls1[i + 1] = "0"
    return ops


if __name__ == "__main__":
    s1 = "101100"
    s2 = "001011"
    print(minOperations(s1,s2))