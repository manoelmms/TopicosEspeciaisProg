# Tópicos Especiais em Programação - Aula 4
# Manoel Silva - Problem F

def solution(num):
    ans = 0
    while num > 0:
        ans += num
        num = num // 10
    return ans


test_cases = int(input())

for i in range(test_cases):
    string = input().split()
    print(solution(int(string[1])) - solution(int(string[0])))
