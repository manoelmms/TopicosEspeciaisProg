test_cases = int(input())

def permutations(letters, string, solutions={}):
    if len(letters) == 0:
        solutions[string] = 1
    else:
        for i in range(len(letters)):
            letters_copy = letters.copy()
            letters_copy.pop(i)  
            permutations(letters_copy, string + letters[i] , solutions)

for _ in range(test_cases):

    string = sorted(list(input()))
    solutions = {}
    permutations(string, '', solutions)
    
    for solution in solutions:
        print(solution)
    print()


