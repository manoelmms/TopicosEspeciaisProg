# Tópicos Especiais em Programação - Aula 5
# Manoel Silva - Problem B

def extended_euclid(a, b):
    # non-recursive version
    r = a
    r1 = b
    u = 1
    v = 0
    u1 = 0
    v1 = 1

    rs, us, vs, q = 0, 0, 0, 0

    while r1 != 0:
        q = r // r1
        rs = r
        us = u
        vs = v
        r = r1
        u = u1
        v = v1
        r1 = rs - q * r1
        u1 = us - q * u1
        v1 = vs - q * v1
    
    return r, u, v

def main():
    while True:
        try:
            data = input().split()
            a, b = int(data[0]), int(data[1])

            gcd, x, y = extended_euclid(a, b)
            print(x, y, gcd)

        except EOFError:
            break

if __name__ == "__main__":
    main()