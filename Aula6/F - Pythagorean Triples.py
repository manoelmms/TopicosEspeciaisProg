# Tópicos Especiais em Programação - Aula 6
# Manoel Silva - Problem F

# https://github.com/MathProgrammer/CodeForces/blob/master/Explanations/Explanations%20-%207/Pythagorean%20Triples%20Explanation.txt
# Basically, n is even, then n^2 is a multiple of 4, 
# Then, a = root(4k), b = (k - 1), c = (k + 1), k = n^2/4
# If n is odd, a = root(2k+1), b = k, c = k+1, k = (n^2 - 1)/2

number = int(input())

if number <= 2:
    print(-1)
    exit()

if number % 2 == 0: # even
    k = (number**2)//4
    b = k-1
    c = k+1
else: # odd
    k = ((number**2)-1)//2
    b = k
    c = k+1

print(b, c)