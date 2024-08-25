# Tópicos Especiais em Programação - Aula 1
# Manoel Silva - Problem F

test_cases =  int(input())

for i in range(test_cases):
    limit = input().split(" ")
    limit = list(map(int, limit))

    mices = input().split(" ")
    mices = list(map(int, mices))
    mices.sort(reverse=True)

    hole = limit[0]

    steps = 0
    safe = 0
    for m in range(limit[1]):
        if mices[m] > hole:
            break
        else:
            if steps + (hole - mices[m]) >= hole:
                break
            steps += hole - mices[m]
            safe += 1

    print(safe)
    