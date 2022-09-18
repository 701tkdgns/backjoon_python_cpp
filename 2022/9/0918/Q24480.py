import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(r):
    global idx
    for n in lst[r]:
        if visit[n] == 0:
            visit[n] = idx
            idx += 1
            dfs(n)


N, M, R = map(int, input().split())  # 정점 수, 간선 수, 시작 정점
lst = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)
idx = 2
for node in lst:
    node.sort(reverse=True)
visit[R] = 1
dfs(R)
for i in range(1, N + 1):
    print(visit[i])