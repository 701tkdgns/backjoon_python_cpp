import sys

sys.setrecursionlimit(10 ** 6)


def dfs(v):
    print(v, end=' ')
    tmp.append(v)
    for i in lst[v]:
        if not visit[i] and i in lst[v]:
            visit[i] = True
            dfs(i)


N, M = map(int, input().split())
lst = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
chk = False
for e in lst:
    e.sort()
for i in range(N):
    visit = [False for _ in range(N)]
    visit[i] = True
    tmp = []
    dfs(i)
    print()
    if len(tmp) == N:
        break
print(1 if len(tmp) == N else 0)
