while True:
    total = int(input())
    if total == 0:
        break

    c1, n1 = map(int, input().split())
    c2, n2 = map(int, input().split())

    if (c1/n1) < (c2/n2):
        cheapest = n1
        exp = n2
    else:
        cheapest = n2
        exp = n1
    
    max_box_cheapest = total//cheapest
    n_box_exp = 0
    while max_box_cheapest > 0:
        if max_box_cheapest*cheapest + n_box_exp*exp == total:
            break
        else:
            max_box_cheapest -= 1
            n_box_exp += 1
    print(max_box_cheapest, n_box_exp)
            
