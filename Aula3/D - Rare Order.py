# Tópicos Especiais em Programação - Aula 3
# Manoel Silva - Problem D

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

def order(str):
    letters = set()
    graph = {}
    idg = {}

     # Creating set of letters that appear in all lines
    letters.update(set("".join(string)))

    # Creating graph and in-degree
    for letter in letters:
        graph[letter] = []
        idg[letter] = 0

    # Creating graph
    for i in range(len(str)-1):
        word1 = str[i]
        word2 = str[i+1]
        min_len = min(len(word1), len(word2))

        for j in range(min_len):
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j])
                idg[word2[j]] += 1
                break

    result = topological_sort(idg, graph)
    print("".join(result))


if __name__ == "__main__":

    data = sys.stdin.readline().strip()
    string = []

    while data != '#':
        string.append(data)
        data = sys.stdin.readline().strip()
    order(string)

