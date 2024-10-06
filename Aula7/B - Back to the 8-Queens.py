# According to Wikipedia, the 8 queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal.
# But we can brute force it because we have only 92 cases to check.
def queens(n: int, i: int, a: list, b: list, c: list):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j]) # Very cool use of yield in Python, it's like a return but it doesn't stop the function
    else:
        yield a

def main():
    case_number = 1
    solutions = list(queens(8, 0, [], [], []))
    while True:
        try:
            position = list(map(int, input().split()))
            for i in range(8):
                position[i] -= 1
            min_moves = 8
            for solution in solutions:
                moves = 0
                for i in range(8):
                    if solution[i] != position[i]:
                        moves += 1
                min_moves = min(min_moves, moves)
            print("Case {}: {}".format(case_number, min_moves))
            case_number += 1
        except EOFError:
            break
            
if __name__ == '__main__':
    main()
