# Tópicos Especiais em Programação - Aula 5
# Manoel Silva - Problem A

def max_factor(n):

    if n < 0:
        n *= -1

    result = -1
    counter = 0

    i = 2
    while i * i <= n and n != 1: # while i is less than the square root of n
        while n % i == 0: # if n is divisible by i
            result = i # update result to i
            n = n // i # divide n by i
        if result == i: # if n is divisible by i
            counter += 1
        i += 1 # increment i

    if n != 1 and result != -1: # case where n is prime, so result is n
        result = n 
    elif counter == 1: # Its not dibilisible by any number other than 1 and itself
        result = -1

    return result

def main():
    while True:
        number = int(input())
        if number == 0:
            break

        print(max_factor(number))

if __name__ == "__main__":
    main()



            