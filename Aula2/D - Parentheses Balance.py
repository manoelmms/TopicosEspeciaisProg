# Tópicos Especiais em Programação - Aula 2
# Manoel Silva - Problem D

def is_balanced(expression):
    stack = []
    for c in expression:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif c == ']' and stack and stack[-1] == '[':
            stack.pop()
        else:
            return False
    return not stack

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        expression = input()
        if is_balanced(expression):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
