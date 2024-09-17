# Tópicos Especiais em Programação - Aula 6
# Manoel Silva - Problem E

while True:
    try:
        B = input()
        if B == '':
            continue
        B = int(B)
        P = int(input())
        M = int(input())

        result = pow(B,P,M)
        print(result)

    except EOFError:
        break