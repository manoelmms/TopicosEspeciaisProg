# Tópicos Especiais em Programação - Aula 2
# Manoel Silva - Problem C

dict = {}
while True:
    word = input()
    if word == "#":
        break
    word = word.split(" ")
    for w in word:
        key = "".join(sorted(w.lower()))
        if key in dict:
            dict[key].append(w)
        else:
            dict[key] = [w]


result = []
for key in sorted(dict.keys()):
    if len(dict[key]) == 1:
        result.append(dict[key][0])
        
result.sort()
for r in result:
    print(r)
