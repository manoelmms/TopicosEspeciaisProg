lines = int(input())
fila = []
for i in range(lines):
    string = list(input().split())
    if string[0] == "Sleep":
        fila.append(string[1])
    elif string[0] == 'Kick':
        if len(fila) > 0:
            fila.pop()
    elif string[0] == 'Test':
        if len(fila) == 0:
            print("Not in a dream")
        else:
            print(fila[-1])
