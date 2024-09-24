while True:
    n = int(input())
    if n == 0:
        break
    m = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    dominoes = []
    for i in range(m):
        dominoes.append(list(map(int, input().split())))

    

