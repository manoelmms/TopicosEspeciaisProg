# Tópicos Especiais em Programação - Aula 4
# Manoel Silva - Problem A

import sys

cases = int(sys.stdin.readline().strip())

for case in range(cases):
    # Multiple of 60 needs to be a multiple of 2,3 and 10 at the same time 
    sum = 0
    multiple_2 = 0
    zero_exists = False
    
    number = sys.stdin.readline().strip()

    for digit in number:
        if digit == "0":
            zero_exists = True
        if int(digit) % 2 == 0:
            multiple_2 += 1 # Counting the number of multiples of 2
        sum += int(digit)

    # If the sum is multiple of 3, there is a zero and there are more than one multiple of 2
    # More than one multiple of 2 is needed because 2 is a factor of 6
    if sum % 3 == 0 and zero_exists and multiple_2 > 1:
        print('red')
    else:
        print('cyan')
