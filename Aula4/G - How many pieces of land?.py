# Tópicos Especiais em Programação - Aula 4
# Manoel Silva - Problem G

import math
test_cases = int(input())

for i in range(test_cases):
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    elif n == 4:
        print(8)
    else:
        # F = A - V + 2
        n = n - 1
        F = 1 + n + (n*(n-1))//2 + (n*(n-1)*(n-2)*(n-3))//24 + (n*(n-1)*(n-2))//6

        print(int(F))

