def find(parent: list, x: int):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: list, x: int, y: int):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        parent[rootX] = rootY


P = int(input())
G = int(input())
parent = list(range(G + 1))
count = 0
for _ in range(G):
    gate = int(input())
    root = find(parent, gate)
    if root == 0: break
    union(parent, root, root - 1)
    count += 1
print(count)

# def find(parent, x):
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]
#
#
# def union(parent, x, y):
#     rootX = find(parent, x)
#     rootY = find(parent, y)
#     if rootX != rootY:
#         parent[rootX] = rootY
#
#
# G = int(input())
# P = int(input())
# gateway = [i for i in range(G + 1)]
# count = 0
# for _ in range(P):
#     g = int(input())
#     root = find(gateway, g)
#     if root == 0: break
#     union(gateway, root, root - 1)
#     count += 1
# print(count)
