def maximum_winning_streak(bets):
    ans = 0
    streak = 0
    for i in range(len(bets)):
        streak += bets[i]
        if streak < 0:
            streak = 0 # reset the streak if it becomes negative, because if it's negative, it's better to start over
        ans = max(ans, streak) 
    return ans

while True:
    try:
        l = input()
        if l == '':
            continue
        l = int(l)
        if l == 0:
            break

        bets = []
        while len(bets) < l:
            line = input().split()
            for bet in line:
                bets.append(int(bet))
        
        ans = maximum_winning_streak(bets)
        if ans > 0:
            print(f'The maximum winning streak is {ans}.')
        else:
            print('Losing streak.')
    except EOFError:
        break
