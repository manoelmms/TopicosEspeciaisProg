import math
test_cases = int(input())

for i in range(test_cases):
    taml_1, tam_l2 = map(int, input().split())
    l_1 = list(map(int, input().split()))
    l_2 = list(map(int, input().split()))

    dict_1 = {}
    dict_2 = {}

    for i in l_1:
        if i not in dict_1:
            dict_1[i] = 0
        dict_1[i] += 1
    for i in l_2:
        if i not in dict_2:
            dict_2[i] = 0
        dict_2[i] += 1
    
    min_found = 0
    
    for num in dict_1:
        if num not in dict_2:
            min_found += dict_1[num]
        else:
            dist = abs(dict_2[num] - dict_1[num])
            min_found += dist
    
    for num in dict_2:
        if num not in dict_1:
            min_found += dict_2[num]

    print(min_found)
