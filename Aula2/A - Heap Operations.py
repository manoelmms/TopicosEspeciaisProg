# Tópicos Especiais em Programação - Aula 2
# Manoel Silva - Problem A

# insert - cod 0
# getmin - cod 1
# removeMin - cod 2

import heapq

heap = []
heapq.heapify(heap)
instructions = []

instructions_count = int(input())

for i in range(instructions_count):
    operation = input()
    instruction = operation.split()

    if len(instruction) == 1: # removeMin
        if len(heap) == 0:
            instructions.append('insert 32')
            instructions.append('removeMin')
        else:
            heapq.heappop(heap)
            instructions.append('removeMin')
    elif instruction[0] == 'insert':
        heapq.heappush(heap, int(instruction[1])) 
        instructions.append(operation)
    else: #getMin
        new_min = int(instruction[1])
        
        while len(heap) > 0 and heap[0] < new_min:
            heapq.heappop(heap)
            instructions.append('removeMin')

        if len(heap) == 0 or heap[0] != new_min:
            heapq.heappush(heap, new_min) 
            instructions.append(f'insert {new_min}')

        instructions.append(operation)

print(len(instructions))

for instruction in instructions:
    print(instruction)
