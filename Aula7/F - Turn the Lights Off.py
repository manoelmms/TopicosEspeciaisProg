def button_press(matrix, i, j):
    matrix[i][j] = not matrix[i][j]
    if i > 0:
        matrix[i-1][j] = not matrix[i-1][j]
    if i < 9:
        matrix[i+1][j] = not matrix[i+1][j]
    if j > 0:
        matrix[i][j-1] = not matrix[i][j-1]
    if j < 9:
        matrix[i][j+1] = not matrix[i][j+1]

def combinations_first_row():
    combinations = []
    for i in range(2**10):
        combination = []
        for j in range(10):
            combination.append(i & 1) # i & 1 [bitwise and]
            i >>= 1 # i = i >> 1 [shift right, divide by 2]
        combinations.append(combination)
    return combinations

def solve(matrix):
    min_presses = 0 # minimum number of presses
    combinations = combinations_first_row()

    for combination in combinations:
        matrix_copy = [row.copy() for row in matrix]
        presses = 0
        for j in range(10):
            if combination[j]:
                button_press(matrix_copy, 0, j)
                presses += 1
        for i in range(1, 10):
            for j in range(10):
                if matrix_copy[i-1][j]:
                    button_press(matrix_copy, i, j)
                    presses += 1
        if all(not cell for cell in matrix_copy[9]):
            if min_presses == 0 or presses < min_presses:
                min_presses = presses
    return -1 if min_presses > 100 else min_presses

while True:
    case_name = input()
    if case_name == 'end':
        break

    matrix = []
    for i in range(10):
        matrix.append(list(input()))
    # switching 0 for True and # for False
    for i in range(10):
        for j in range(10):
            matrix[i][j] = True if matrix[i][j] == 'O' else False

    result = solve(matrix)
    print(case_name, result)
