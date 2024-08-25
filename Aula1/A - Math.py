# Tópicos Especiais em Programação - Aula 1
# Manoel Silva - Problem A

# for i in range(100):
#     result = ((1**i)+(2**i)+(3**i)+(4**i))
#     result = result % 5

#     print(f"i={i}, result={result}")

number = int(input())

if ((number %4) == 0):
    print('4')
else:
    print('0')