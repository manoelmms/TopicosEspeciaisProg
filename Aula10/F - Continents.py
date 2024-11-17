class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y

            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x

            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def find_groups(mapa):
    m = len(mapa)
    n = len(mapa[0]) if m > 0 else 0
    uf = UnionFind(m * n)

    def get_index(i, j):
        return i * n + j

    for i in range(m):
        for j in range(n):
            char = mapa[i][j]
            up_char = mapa[i - 1][j] if i > 0 else None
            down_char = mapa[i + 1][j] if i < m - 1 else None
            left_char = mapa[i][j - 1] if j > 0 else None
            right_char = mapa[i][j + 1] if j < n - 1 else mapa[i][0]

            if up_char == char:
                uf.union(get_index(i, j), get_index(i - 1, j))
            if down_char == char:
                uf.union(get_index(i, j), get_index(i + 1, j))
            if left_char == char:
                uf.union(get_index(i, j), get_index(i, j - 1))
            if right_char == char:
                uf.union(get_index(i, j), get_index(i, j + 1 if j < n - 1 else 0))


    ds = {}
    for i in range(m):
        for j in range(n):
            char = mapa[i][j]
            if char not in ds:
                ds[char] = {}
            root = uf.find(get_index(i, j))
            if root in ds[char]:
                ds[char][root].append((i, j))
            else:
                ds[char][root] = [(i, j)]

    return ds
            

while True:
    try:
        m, n = map(int, input().split())
        mapa = []
        for _ in range(m):
            line = input()
            mapa.append(list(line[:n]))

        coords = tuple(map(int, input().split()))
        input()  # Linha em branco

        init_char = mapa[coords[0]][coords[1]]
        ds = find_groups(mapa)

        biggest_group = 0
        for set_id, group in ds[init_char].items():
            if coords not in group:
                biggest_group = max(biggest_group, len(group))
        print(biggest_group)

    except EOFError:
        break
