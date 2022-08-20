import sys

sys.setrecursionlimit(10 ** 6)
std = sys.stdin.readline

n, m = map(int, std().split())
parent = [i for i in range(n + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    chk, a, b = map(int, std().split())
    if chk == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
    print(parent)