import sys
sys.setrecursionlimit(10**9)
def dfs(v):
    for i in lst[v]:
        if visit[i] == 0:
            visit[i] = v
            dfs(i)

N = int(input())
lst = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
dfs(1)
for i in range(2, N + 1):
    print(visit[i])