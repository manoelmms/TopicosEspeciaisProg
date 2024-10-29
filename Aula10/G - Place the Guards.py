from collections import defaultdict

def dfs(nd, color, graph):
    global total, guards
    total += 1
    if color[nd] == 1:
        guards += 1
    for neighbor in graph[nd]:
        if color[neighbor] == 0:
            color[neighbor] = 3 - color[nd] 
            if not dfs(neighbor, color, graph):
                return False
        elif color[neighbor] == color[nd]:
            return False
    return True

test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    color = [0] * (n + 1)

    ans = 0
    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            total = 0
            guards = 0
            if not dfs(i, color, graph):
                ans = -1
                break
            ans += max(1, min(guards, total - guards)) if total > 1 else guards
    print(ans)

