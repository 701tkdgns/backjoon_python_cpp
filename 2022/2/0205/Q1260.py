from collections import deque


def init():
    return [False for _ in range(N + 1)]


def dfs(v):
    visit[v] = True
    print(v, end=' ')
    for i in lst[v]:
        if not visit[i]:
            dfs(i)


def bfs(v):
    dq = deque([v])
    visit[v] = True
    while dq:
        v = dq.popleft()
        print(v, end=' ')
        for i in lst[v]:
            if not visit[i]:
                dq.append(i)
                visit[i] = True


N, M, V = map(int, input().split())
lst = [[] for _ in range(N + 1)]
visit = init()
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for e in lst:
    e.sort()
dfs(V)
print()
visit = init()
bfs(V)
