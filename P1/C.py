import math

import math

def sieve(n):
    size = n//2
    sieve = [True]*size
    limit = int(math.sqrt(n)+1)

    for i in range(1, limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [False]*tmp

    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i > 0]

def prime_factorization(n, primes):
    factors = {}
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            n //= p
            factors[p] = factors.get(p, 0) + 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def LCM(a,b):
    a*b/math.gcd(a,b)

c = sieve(30000)
while True:
    n = int(input())
    if n == 0:
        break

    

    