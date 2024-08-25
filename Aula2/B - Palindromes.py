# Tópicos Especiais em Programação - Aula 2
# Manoel Silva - Problem B

reverse = { 'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J', 'M': 'M',
            'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
            'Y': 'Y', 'Z': '5', '1': '1', '2': 'S', '3': 'E', '5': 'Z', '8': '8' }

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

def is_mirrored(word):
    for i in range(len(word)):
        if word[i] != reverse.get(word[-i-1]):
            return False
    return True

def main():
    while True:
        try:
            word = input()
            if is_palindrome(word) and is_mirrored(word):
                print(f"{word} -- is a mirrored palindrome.")
            elif is_palindrome(word):
                print(f"{word} -- is a regular palindrome.")
            elif is_mirrored(word):
                print(f"{word} -- is a mirrored string.")
            else:
                print(f"{word} -- is not a palindrome.")
            print()
        except EOFError:
            break

if __name__ == '__main__':
    main()
