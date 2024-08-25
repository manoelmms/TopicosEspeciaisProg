# Tópicos Especiais em Programação - Aula 1
# Manoel Silva - Problem B

test_cases =  int(input())

for i in range(test_cases):
    candy_types = int(input())
    candy = input().split(" ")
    candy = list(map(int, candy))
    
    if candy_types == 1 and candy[0] == 1:
        print("YES")
        continue
    elif candy_types == 1 and candy[0] != 1:
        print("NO")
        continue

    candy.sort() # Sort the list of candies

    if (candy[-1] - 1) <= candy[-2]:
        print("YES")
    else:
        print("NO")



            
