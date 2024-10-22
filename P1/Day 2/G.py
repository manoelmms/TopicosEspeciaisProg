test_cases = int(input())

for i in range(test_cases):
    s = list(input())
    t = list(input())

    s_0 = []
    s_1 = []
    s_q = []

    t_0 = []
    t_1 = []

    min_moves = 0

    for i in range(len(s)):
        cs = s[i]    
        if cs == '1':
            s_1.append(i)
        elif cs == '0': 
            s_0.append(i)
        else: # ?
            s_q.append(i)
    
    for i in range(len(t)):
        ct = t[i]    
        if ct == '1':
            t_1.append(i)
        elif ct == '0': 
            t_0.append(i)

    if len(t_1) > len(s_q):
        min_moves = -1
    else:
        min_moves += len(s_q)

    

