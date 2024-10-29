def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    if rank[x] > rank[y]:
        rank[x] += rank[y]
        parent[y] = x
    else:
        rank[y] += rank[x]
        parent[x] = y

test_cases = int(input())

for _ in range(test_cases):
    n,m = map(int, input().split())
    parent = [i for i in range(n+1)]
    rank = [1 for _ in range(n+1)]
    for _ in range(m):
        x,y = map(int, input().split())
        x = find(x)
        y = find(y)
        if x != y:
            union(x, y)
    print(max(rank))