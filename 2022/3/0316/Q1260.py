from collections import deque


def init():
    return [False] * (N + 1)


def dfs(v):
    dfs_chk[v] = True
    print(v, end=' ')
    for i in lst[v]:
        if not dfs_chk[i]:
            dfs(i)


def bfs(v):
    dq = deque([v])
    bfs_chk[v] = True
    while dq:
        v = dq.popleft()
        print(v, end=' ')
        for i in lst[v]:
            if not bfs_chk[i]:
                dq.append(i)
                bfs_chk[i] = True


N, M, V = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for s in lst:
    s.sort()
dfs_chk = init()
dfs(V)
print()
bfs_chk = init()
bfs(V)
