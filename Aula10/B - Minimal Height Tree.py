test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    a =[int(x) for x in input().split()]

    h = 1 # altura mínima da árvore
    p,q = 0, 0

    for i in range(1, len(a)):
        if a[i] > a[i-1]:
            p += 1
        else:
            if not q:
                h += 1
                q = p - 1
            else:
                q -= 1

    print(h)
