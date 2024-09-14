# Tópicos Especiais em Programação - Aula 5
# Manoel Silva - Problem D

# def sieve(n):
#     size = n//2
#     sieve = [True]*size
#     limit = int(math.sqrt(n)+1)

#     for i in range(1, limit):
#         if sieve[i]:
#             val = 2*i+1
#             tmp = ((size-1) - i)//val
#             sieve[i+val::val] = [False]*tmp

#     return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i > 0]


def sieve(n):
    numbers = [True]*(n+1)
    numbers[0] = numbers[1] = False
    primes = []

    for number, prime in enumerate(numbers):
        if prime:
            primes.append(number)
            for i in range(2*number, n+1, number):
                numbers[i] = False

    return numbers

def charmichael(n, primes):
    if n%2 == 0:
        return False
    if primes[n]:
        return False
    for a in range(2, n-1):
        a %= n # a = a mod n
        if pow(a, n, n) != a: # Fermat's little theorem a^(n-1) = 1 mod n
            return False
    return True

def main():

    tam = 65000
    primes = sieve(tam)

    while True:
        number = int(input())
        if number == 0:
            break

        if charmichael(number, primes):
            print("The number {} is a Carmichael number.".format(number))
        else:
            print("{} is normal.".format(number))

if __name__ == '__main__':
    main()
