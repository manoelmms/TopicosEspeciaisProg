# Tópicos Especiais em Programação - Aula 6
# Manoel Silva - Problem B
import math

test_cases = int(input())

for _ in range(test_cases):
    array = list(map(int, input().split()))
    max = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            aux = math.gcd(array[i], array[j])
            if aux > max:
                max = aux
    print(max)
