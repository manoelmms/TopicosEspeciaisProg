# Tópicos Especiais em Programação - Aula 3
# Manoel Silva - Problem F

while True:
    s = input()
    if s == ".":
        break

    n = len(s)
    for i in range(1, n+1):
        if n % i == 0: # Se o tamanho da substring for um divisor do tamanho da string
            p = n // i # Quantas vezes a substring se repete
            if s == s[:i] * p: # Se a string for igual a substring * p
                print(p)
                break
