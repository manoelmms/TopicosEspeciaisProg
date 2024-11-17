def dfs(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def is_eurelian(graph):
    flag = False
    for node in graph:
        if len(graph[node]) % 2 == 1:
            flag = True
    return flag


while True:
    try:
        n, r = map(int, input().split())
        graph = {}
        for i in range(r):
            c1, c2 = map(int, input().split())
            if c1 not in graph:
                graph[c1] = {}
            if c2 not in graph:
                graph[c2] = {}
            graph[c1][c2] = 1
            graph[c2][c1] = 1

        if not is_eurelian(graph):
            print("Not Possible")
        else:
            visited = [False] * n
            count = 0
            for node in graph:
                if not visited[node]:
                    dfs(graph, node, visited)
                    count += 1
            if count == 1: 
                print("Possible")
            else:
                print("Not Possible")
            
    except EOFError:
        break