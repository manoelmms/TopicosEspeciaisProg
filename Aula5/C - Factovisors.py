# Tópicos Especiais em Programação - Aula 5
# Manoel Silva - Problem C

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
        
def fatorial_fatorizado(n, primes):
    fatores = {}
    for i in range(2, n+1):
        fatores_i = prime_factorization(i, primes)
        for fator, expoente in fatores_i.items():
            fatores[fator] = fatores.get(fator, 0) + expoente
    return fatores

def solve_1(number, factorial, primes):
    fatores_num = prime_factorization(number, primes)
    fatores_fatorial = fatorial_fatorizado(factorial, primes)

    for fator, expoente in fatores_num.items():
        if fator not in fatores_fatorial or fatores_fatorial[fator] < expoente:
            print("{} does not divide {}!".format(number, factorial))
            return
        else:
            fatores_fatorial[fator] -= expoente

    print("{} divides {}!".format(number, factorial))
    
def solve_2(number, factorial, primes):
    fatores_num = prime_factorization(number, primes)
    
    for fator, expoente in fatores_num.items():
        t_freq = 0
        temp = fator
        while temp <= factorial: # conta quantas vezes fator divide factorial
            t_freq += factorial//temp
            temp *= fator
        if t_freq < expoente: # se a quantidade de fatores fator em factorial for menor que a quantidade de fatores fator em number, number não divide factorial
            print("{} does not divide {}!".format(number, factorial))
            return
        
    print("{} divides {}!".format(number, factorial))


def main():
    primes = sieve(30000)
    while True:
        try:
            entrada = input().split()
            n = int(entrada[0])
            m = int(entrada[1])
            solve_1(m, n, primes)
        except EOFError:
            break

if __name__ == "__main__":
    main()

