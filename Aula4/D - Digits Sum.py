# Tópicos Especiais em Programação - Aula 4
# Manoel Silva - Problem D

test_cases = int(input())

for i in range(test_cases):
    number = int(input())
    
    last_digit = number % 10
    last_digit_nine = True if last_digit == 9 else False
    remaining = number // 10

    if last_digit_nine:
        remaining += 1

    print(remaining)