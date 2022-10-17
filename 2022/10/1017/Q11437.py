import sys

sys.setrecursionlimit(10 ** 6)


def tree(v, depth):
    visit[v] = True
    dp[v] = depth
    for i in lst[v]:
        if not visit[i]:
            parent[i] = v
            tree(i, depth + 1)

# 최소 공통 조상 찾기
def lca(a, b):
    # 깊이 맞추기
    while dp[a] != dp[b]:
        if dp[a] > dp[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 노드 맞추기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a



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
    lca(a, b)