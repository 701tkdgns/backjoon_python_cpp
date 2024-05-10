from collections import deque

def dfs(v):
    if not visit[v]:
        print(v, end=' ')
        visit[v] = 1
        for i in lst[v]:
            dfs(i)

def bfs(v):
    dq = deque([v])
    visit[v] = 1
    while dq:
        x = dq.popleft()
        print(x, end=' ')
        for i in lst[x]:
            if not visit[i]:
                dq.append(i)
                visit[i] = 1

N, M, V = map(int, input().split())
lst = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()
dfs(V)
print()
visit = [0 for _ in range(N + 1)]
bfs(V)