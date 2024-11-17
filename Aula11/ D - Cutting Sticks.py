def cut(i, j, cuts, memo):
    if i + 1 == j:
        return 0

    if (i, j) in memo:
        return memo[(i, j)]

    ans = float('inf')
    for k in range(i+1, j):
        ans = min(ans, cuts[j] - cuts[i] + cut(i, k, cuts, memo) + cut(k, j, cuts, memo))

    memo[(i, j)] = ans
    return ans

while True:
    l = int(input())
    if l == 0:
        break

    n = int(input())
    
    cuts = list(map(int, input().split()))
    cuts.insert(0, 0)
    cuts.append(l)

    memo = {}
    print(f'The minimum cutting is {cut(0, n+1, cuts, memo)}.')     