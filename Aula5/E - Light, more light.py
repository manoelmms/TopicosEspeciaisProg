# Tópicos Especiais em Programação - Aula 5
# Manoel Silva - Problem E

import math

while True:
    number = int(input())

    if number == 0:
        break

    test = math.isqrt(number)**2
    if test == number:
        print("yes")
    else:
        print("no")
