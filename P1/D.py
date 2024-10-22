test_cases = int(input())

for i in range(test_cases):
    n = int(input())
    if n == 0:
        print("0")
        continue
    vec = []
    for j in range(n):
        vec.append(int(input()))
    
    s = set()
    size = 0
    l = 0

    for j in range(n):
        while vec[j] in s:
            s.remove(vec[j])
            l += 1
        s.add(vec[j])
        size = max(size, j-l+1)
    
    print(size)
