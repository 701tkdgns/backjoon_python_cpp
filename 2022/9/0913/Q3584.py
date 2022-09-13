import sys
sys.setrecursionlimit(10**6)


def tree(n, idx):
    if n == S or n == E:
        return idx
    pass


T = int(input())
for _ in range(T):
    N = int(input())
    lst = [[] for _ in range(N + 1)]
    dist = [-1 for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    S, E = map(int, input().split())
    tree(1, 1)