for _ in range(int(input())):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    # Subtracting C as it will in the end be subtracted from every operation
    for i in range(n):
        a[i] -= c
    
    # We can Perform Operation 1 add value to the total for all positive numbers
    # However the Operation 2 to pick 2 numbers and add the maximum to the total 
    # can be done by picking 1 positive and 1 negative number
    # Operation 2 can be done at max n // 2 times --> m times
    # if there are more positive values(p) than m then we will add every p value to the total
    # if there are less then we make the first m values as 0 as we will be clubbing them with the highest pososible
    for i in range(n//2):
        # This loop runs till m times and if p > m then we get the value as a[i] else we get 0
        a[i] = max(a[i], 0)
    print(sum(a))