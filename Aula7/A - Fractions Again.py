def pairs(n):
    possible_pairs = []
    for i in range(n+1, 2*n+1): # 2*n+1 is not included, max value is 2*n
        if (n*i)%(i-n) == 0: # (n*i)/(i-n) is an integer number
            possible_pairs.append(((n*i)//(i-n), i))
    return possible_pairs

def main():
    while True:
        try:
            n = int(input())
            possible_pairs = pairs(n)
            print(len(possible_pairs))
            for pair in possible_pairs:
                print("1/{} = 1/{} + 1/{}".format(n, pair[0], pair[1]))
        except EOFError:
            break

if __name__ == '__main__':
    main()
