import sys
sys.setrecursionlimit(100000)

def dfs(v):
    if not visit[v]:
        visit[v] = True
        tmp.append(v)
        for i in lst[v]:
            if not visit[i]:
                dfs(i)

def bfs(v):
    if visit[v]:
        return
    queue, tmp = [v], []
    while queue:
        v = queue[0]
        del queue[0]
        if not visit[v]:
            tmp.append(v)
            visit[v] = True
            for i in lst[v]:
                if not visit[i]:
                    queue.append(i)
    if tmp and tmp not in res:
        res.append(set(tmp))


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
visit = [False for _ in range(N + 1)]
res = []
for i in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()
for i in range(1, N + 1):
    tmp = []
    dfs(i)
    if tmp and tmp not in res:
        res.append(tmp)
print(len(res))
