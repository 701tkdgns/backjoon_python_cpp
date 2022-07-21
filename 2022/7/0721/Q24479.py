import sys

sys.setrecursionlimit(100000)

def dfs(v):
    global cnt
    visit[v] = cnt
    lst[v].sort()
    for l in lst[v]:
        if visit[l] == 0:
            cnt += 1
            dfs(l)


N, M, R = map(int, input().split())
lst = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
cnt = 1

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

dfs(R)
for i in range(1, N + 1):
    print(visit[i])