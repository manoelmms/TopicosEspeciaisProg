# Tópicos Especiais em Programação - Aula 3
# Manoel Silva - Problem C

import sys

def topological_sort(in_degree, graph):
    queue = []
    result = []
    for i in in_degree:
        if in_degree[i] == 0:
            queue.append(i)
    
    while queue:
        u = queue.pop(0)
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return result

if __name__ == "__main__":
    while True:
        n, m = list(map(int, sys.stdin.readline().strip().split(" ")))
        if n == 0 and m == 0:
            break

        idg = {}
        graph = {}

        for i in range(1, n+1):
            idg[i] = 0
            graph[i] = []

        for i in range(m):
            e , v = list(map(int, sys.stdin.readline().strip().split(" ")))
            idg[v] += 1
            graph[e].append(v)
            
        result = topological_sort(idg, graph)
        print(" ".join(map(str, result)))

