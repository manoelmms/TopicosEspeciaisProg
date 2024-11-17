test_cases = int(input())

for i in range(test_cases):
    n, m, k = map(int, input().split())

    grid = []
    for j in range(n):
        grid.append(list(map(int, input().split())))

# reducing the problem to a 1D array
    area = [0] * n
    
    for j in range(n):
        