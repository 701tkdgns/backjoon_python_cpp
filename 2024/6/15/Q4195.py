def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        number[x] = number[x] + number[y]
    print(number[x])


N = int(input())
for _ in range(N):
    F = int(input())
    parent, number = {}, {}
    for i in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)