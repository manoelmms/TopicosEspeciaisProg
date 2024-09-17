# Tópicos Especiais em Programação - Aula 6
# Manoel Silva - Problem D

def ordering(array):
    # 1 to 100
    count = [0]*101
    for i in range(len(array)):
        num = array[i]
        count[num] += 1
    return count
    
def print_count(result_array):
    string = ''
    for i in range(len(result_array)):
        x = result_array[i]
        for _ in range(x):
            string += str(i) + ' '
        # removing last space
    string = string[:-1]
    print(string)

while True:
    size = int(input())
    if size == 0:
        break
    array = list(map(int, input().split()))

    print_count(ordering(array))

