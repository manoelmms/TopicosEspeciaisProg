# Tópicos Especiais em Programação - Aula 2
# Manoel Silva - Problem E

test_cases = int(input())

for r in range(test_cases):
    safe = set()
    up = set()
    down = set()
    suspect = None

    for i in range(3):
        left, right, balance = input().split()
        left = set(left)
        right = set(right)

        if balance == "even": # Ambos os lados são iguais, safe
            safe.update(left)
            safe.update(right)

        elif balance == "up": # O lado direito é mais leve, logo os que estavam para baixo antes e os que estavam para cima agora são seguros
            safe.update(down & right)
            safe.update(up & left)

            up.update(right)
            down.update(left)

            if not suspect:
                suspect = left | right
            else:
                suspect &= left | right

        elif balance == "down": # O lado esquerdo é mais leve, logo os que estavam para cima antes e os que estavam para baixo agora são seguros
            safe.update(up & right)
            safe.update(down & left)

            up.update(left)
            down.update(right)

            if not suspect:
                suspect = left | right
            else:
                suspect &= left | right

        up -= safe
        down -= safe

        if not suspect is None:
            up &= suspect
            down &= suspect

    if not len(down):
        print(f"{list(up)[0]} is the counterfeit coin and it is light.")
    else:
        print(f"{list(down)[0]} is the counterfeit coin and it is heavy.")

