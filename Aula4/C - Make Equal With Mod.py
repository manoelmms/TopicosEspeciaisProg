# Tópicos Especiais em Programação - Aula 4
# Manoel Silva - Problem C

test_cases = int(input())

def make_equal(array):
    array.sort()
    has_zero = False
    has_one = False

    if 1 in array:
        has_one = True

    if 0 in array:
        has_zero = True

    if has_zero and has_one:
        return False
    
    elif has_one and not has_zero:
        for i in range(1, len(array)):
            if array[i] - array[i-1] == 1: # If the difference between two consecutive elements is 1, so the array cant be made equal
                return False
        return True
    
    else: 
        return True

for i in range(test_cases):
    array_size = int(input())
    array = list(map(int, input().split()))

    if make_equal(array):
        print("YES")
    else:
        print("NO")
    