# Tópicos Especiais em Programação - Aula 1
# Manoel Silva - Problem E

test_cases =  int(input())

for i in range(test_cases):
    number_string = input()
    number = int(number_string)

    # If the number is divisible by 25, the last two digits are 00, 25, 50 or 75
    pair = ['00', '25', '50', '75']
    
    res_list = []
    for i in pair:
        # finding the first digit
        pos2 = number_string.rfind(i[1])
        pos1 = number_string.rfind(i[0], 0, pos2) # find the first digit before the second digit

        if pos1 != -1 and pos2 != -1: # if both digits are found
            res_list.append(len(number_string) - pos2 - 1 + pos2 - pos1 - 1)

    if len(res_list) == 0:
        print("0")

    else:
        print(min(res_list))

        
            

