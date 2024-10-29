from math import gcd

# Dicionários para rastrear vértices descobertos e para armazenar relações entre vértices
visited = {}
graph = {}

def dfs(graph, start, target):

    if not visited[start]:
        visited[start] = True
        if target in graph[start]:
            return graph[start][target]
        else:
            for neighbor in graph[start].keys():
                result = dfs(graph, neighbor, target)
                if result != "?" and result is not None:
                    return graph[start][neighbor] * result
            return "?"

while True:
    entry = input()
    if entry == ".":
        break
    
    entry_parts = entry.split()
    if entry_parts[0] == "!":
        v1 = entry_parts[1]
        v2 = entry_parts[4]
        s1 = entry_parts[2]
        s2 = entry_parts[5]

        # Calcula o MDC dos valores fornecidos
        factor_gcd = gcd(int(v2), int(v1))
        value_a = int(int(v2) / factor_gcd)
        value_b = int(int(v1) / factor_gcd)
        
        # Atualiza o grafo para refletir as relações bidirecionais entre os vértices
        if s1 not in graph:
            graph[s1] = {s2: value_a}
            visited[s1] = False
        else:
            graph[s1][s2] = value_a

        if s2 not in graph:
            graph[s2] = {s1: value_b}
            visited[s2] = False
        else:
            graph[s2][s1] = value_b
            
    else:
        # Realiza buscas para encontrar as relações entre os vértices
        coefficient_a = dfs(graph, entry_parts[1], entry_parts[3])
        for key in visited.keys():
            visited[key] = False  # Reseta o estado de visitado para cada vértice
        
        coefficient_b = dfs(graph, entry_parts[3], entry_parts[1])
        for key in visited.keys():
            visited[key] = False
        
        # Simplifica o resultado com o MDC e imprime a saída formatada
        if coefficient_a != "?":
            common_divisor = gcd(coefficient_a, coefficient_b)
            coefficient_a = int(coefficient_a / common_divisor)
            coefficient_b = int(coefficient_b / common_divisor)
        
        print(f"{coefficient_b} {entry_parts[1]} = {coefficient_a} {entry_parts[3]}")
