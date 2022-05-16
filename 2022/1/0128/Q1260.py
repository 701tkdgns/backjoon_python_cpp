from collections import deque


def init(n):
    return [False for _ in range(N + 1)]


def dfs(v):
    chk[v] = True
    print(v, end=' ')
    for i in lst[v]:
        if not chk[i]:
            dfs(i)


def bfs(v):
    dq = deque([v])
    while dq:
        v = dq.popleft()
        if not chk[v]:
            chk[v] = True
            print(v, end=' ')
            for i in lst[v]:
                if not chk[i]:
                    dq.append(i)


N, M, V = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()
chk = init(N)
dfs(V)
print()
chk = init(N)
bfs(V)
