test_cases = int(input())

for _ in range(test_cases):
    board = []
    for i in range(3):
        board.append(list(input()))
    try:
        input()
    except EOFError:
        pass
    
    x = 0
    o = 0
    x_wins = False
    o_wins = False

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                x_wins = True
            elif board[i][0] == 'O':
                o_wins = True
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                x_wins = True
            elif board[0][i] == 'O':
                o_wins = True
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                x_wins = True
            elif board[0][0] == 'O':
                o_wins = True
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == 'X':
                x_wins = True
            elif board[0][2] == 'O':
                o_wins = True

    for i in range(3):
        x += board[i].count('X')
        o += board[i].count('O')

    if x < o or x > o + 1:
        print('no')
    elif x_wins and o_wins:
        print('no')
    elif x_wins and x == o:
        print('no')
    elif o_wins and x > o:
        print('no')
    else:
        print('yes')