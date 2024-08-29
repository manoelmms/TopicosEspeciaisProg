# Tópicos Especiais em Programação - Aula 1
# Manoel Silva - Problem G 

test_cases =  int(input())

for i in range(test_cases):
    string = input()
    count_1 = 0
    count_0 = 0
    max_removed = 0

    for letter in string:
        if letter == '1':
            count_1 += 1
        else:
            count_0 += 1

        if count_1 > count_0:
            max_removed = max(max_removed, count_0)
        elif count_0 > count_1:
            max_removed = max(max_removed, count_1)
        
    print(max_removed)
