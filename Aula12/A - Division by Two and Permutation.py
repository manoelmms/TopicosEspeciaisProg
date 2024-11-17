testcases = int(input())

for i in range(testcases):
    l = int(input())
    array = list(map(int, input().split())) 
    seq = [False] * (l+1)
    i = 0    
    while True:
        if i == l:
            yes = True
            break

        if array[i] <= l:
            if seq[array[i]]:
                array[i] = array[i] // 2   
                if array[i] == 0:
                    yes = False 
                    break
            else:
                seq[array[i]] = True
                i+=1
        else:
            array[i] = array[i] // 2

    if yes:
        print('YES')
    else:
        print('NO')
