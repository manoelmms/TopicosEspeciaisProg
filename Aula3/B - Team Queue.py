# Tópicos Especiais em Programação - Aula 3
# Manoel Silva - Problem B

test_cases = 0

while True:
    test_cases += 1
    n = int(input())
    if n == 0:
        break

    print("Scenario #%d" % test_cases)

    team = {}
    team_queue = []
    element_queue = []
    for i in range(n):
        data = input().split(" ")
        for j in range(1, len(data)):
            team[data[j]] = i

    while True:
        command = input().split(" ")
        if command[0] == "STOP":
            break

        if command[0] == "ENQUEUE":
            if team[command[1]] not in team_queue:
                team_queue.append(team[command[1]])
                element_queue.append([command[1]])
            else:
                element_queue[team_queue.index(team[command[1]])].append(command[1])
        if command[0] == "DEQUEUE":
            print(element_queue[0][0])
            element_queue[0].pop(0)
            if len(element_queue[0]) == 0:
                element_queue.pop(0)
                team_queue.pop(0)

    print()
