import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def tree(v, depth):
    visit[v] = True
    dp[v] = depth
    for i in lst[v]:
        if not visit[i]:
            parent[i] = v
            tree(i, depth + 1)


def lca(s, e):
    while dp[s] != dp[e]:
        if dp[s] > dp[e]:
            s = parent[s]
        else:
            e = parent[e]
    while s != e:
        s = parent[s]
        e = parent[e]
    return s


N = int(input())
lst = [[] for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

tree(1, 0)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))