def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        parent[rootX] = rootY


G = int(input())
P = int(input())
parent = list(range(G + 1))
count = 0
for _ in range(P):
    gate = int(input())
    root = find(parent, gate)

    if root == 0:
        break

    union(parent, root, root - 1)
    count += 1

print(count)
