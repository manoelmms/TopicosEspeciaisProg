# Tópicos Especiais em Programação - Aula 3
# Manoel Silva - Problem E

import sys

if __name__ == "__main__":

    while True:
        try:
            data = sys.stdin.readline().strip()
            data = data.split(" ")
            
            if len(data) == 2:
                n = int(data[0])
                password = data[1]
            if len(data) == 1:
                if data[0] == "":
                    break
                n = int(data[0])
                while True:
                    password = sys.stdin.readline().strip()
                    if password != "":
                        break
    
            size = len(password)
            most_common = {}
            for i in range(size-n+1):
                substring = password[i:i+n]
                if substring in most_common:
                    most_common[substring] += 1
                else:
                    most_common[substring] = 1

            print(max(most_common, key=most_common.get))
        
        except EOFError:
            break