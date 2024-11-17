test_cases = int(input())

for _ in range(test_cases):
    n, m = map(int, input().split())
    graph = {}
    
    # Create the graph for max flow
    source = 'source'
    sink = 'sink'

    for i in range(m):
