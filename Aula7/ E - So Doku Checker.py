
while True:
    grid = []
    try:
        for i in range(9):
            grid.append(list(map(int, input().split())))
        input()
    except EOFError:
        break

    solvable = True
    solutions = 0

    print(solve(grid))



        