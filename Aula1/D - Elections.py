# Tópicos Especiais em Programação - Aula 1
# Manoel Silva - Problem D

test_cases =  int(input())

for i in range(test_cases):
    election = input().split(" ")
    election = list(map(int, election))
    
    highest = max(election)
    highest_index = election.index(highest)

    if election[0] == election[1] and election[1] == election[2]:
        print("1 1 1")
        continue

    result = []
    for i in range(3):
        if i == highest_index and election.count(highest) == 1:
            result.append(0)
        else:
            result.append(highest - election[i] + 1)
    
    print(result[0], result[1], result[2])