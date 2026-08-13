def isPrime(n):
    if n <= 1:
        prime = False
    else:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
        return prime
t = int(input())
for _ in range(t):
    n = int(input())
    if isPrime(n + 1):
        print("YES")
    else:
        print("NO")