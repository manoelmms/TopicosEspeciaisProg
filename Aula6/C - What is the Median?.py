# Tópicos Especiais em Programação - Aula 6
# Manoel Silva - Problem C

def sorted_append(array, number):
    if len(array) == 0:
        array.append(number)
        return array
    for i in range(len(array)):
        if number < array[i]:
            array.insert(i, number)
            return array
    array.append(number)

array = []
while True:
    try:
        number = int(input())
        sorted_append(array, number)
        size = len(array)
        if size % 2 == 0:
            median = (array[size//2] + array[size//2 - 1])/2
        else:
            median = array[size//2]

        print(int(median))

    except EOFError:
        break