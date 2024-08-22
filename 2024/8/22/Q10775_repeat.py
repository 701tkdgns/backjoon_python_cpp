import sys
input = sys.stdin.readline

def find(parent: list, x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: list, x: int, y: int) -> None:
    rootX: int = find(parent, x)
    rootY: int = find(parent, y)
    if rootX != rootY:
        parent[rootX] = rootY


G: int = int(input())
P: int = int(input())
gateway = list(range(G + 1))
count: int = 0
for _ in range(P):
    g: int = int(input())
    root = find(gateway, g)
    # print('find : gateway: {}, root: {}'.format(gateway, root))
    if root == 0: break
    union(gateway, root, root - 1)
    # print('find : gateway: {}'.format(gateway))
    count += 1
print(count)