def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        count[x] += count[y]
    print(count[x])

N = int(input())
for _ in range(N):
    F = int(input())
    parent, count = {}, {}
    for _ in range(F):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1
        union(a, b)