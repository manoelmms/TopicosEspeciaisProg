# Tópicos Especiais em Programação - Aula 1
# Manoel Silva - Problem C

test_cases =  int(input())

for i in range(test_cases):
    string = input()
    aux = ''
    tam = len(string)

    for letter in string:
        if letter in aux:
            tam -= 2
            aux = ''
        else:
            aux = aux + letter

    print(tam)

        
