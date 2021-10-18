from math import sqrt

def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def findPrimefactors(s, n) :
    while (n % 2 == 0) :
        s.add(2)
        n = n // 2
    for i in range(3, int(sqrt(n)), 2):
        while (n % i == 0) :
            s.add(i)
            n = n // i
    if (n > 2) :
        s.add(n)

def findPrimitive( n) :
    s = set()
    if (isPrime(n) == False):
        return -1
    phi = n - 1
    findPrimefactors(s, phi)
    for r in range(2, phi + 1):
        flag = False
        for it in s:
            if (power(r, phi // it, n) == 1):
                flag = True
                break
        if (flag == False):
            return r
    return -1

print("Enter a prime number: ")
primeNumber = int(input())

while(isPrime(primeNumber) == False):
    print("The given number is not prime, please try again")
    primeNumber = int(input())

# primitiveRoot = findPrimitive(primeNumber)
print("Enter the second prime number: ")
primeNumber1 = int(input())

while(isPrime(primeNumber1) == False):
    print("The given number is not prime, please try again")
    primeNumber1 = int(input())
primitiveRoot = primeNumber1
# print("The primitive root of", primeNumber, "is", primitiveRoot)

print("Enter private key for user A: ")
privateKeyA = int(input())
publicKeyA = power(primitiveRoot, privateKeyA, primeNumber)
print("The public key for user A is", publicKeyA)

print("Enter private key for user B: ")
privateKeyB = int(input())
publicKeyB = power(primitiveRoot, privateKeyB, primeNumber)
print("The public key for user A is", publicKeyB)

sA = power(publicKeyB, privateKeyA, primeNumber)
sB = power(publicKeyA, privateKeyB, primeNumber)

print("The secret key for user A is", sA)
print("The secret key for user B is", sB)