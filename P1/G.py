import math

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    # boolean array
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    return prime


s = SieveOfEratosthenes(1299710)
while True:
    n = int(input())
    if n == 0:
        break

    if s[n]:
        print(0)
    
    else:
        h = n
        l = n
        while not s[h]:
            h += 1
        while not s[l]:
            l -= 1
        print(h-l)
        
    