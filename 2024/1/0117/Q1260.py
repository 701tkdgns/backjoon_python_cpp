from collections import deque


def dfs(v):
    if dfs_visit[v] == 0:
        print(v, end=" ")
        dfs_visit[v] = 1
        for new_node in lst[v]:
            dfs(new_node)


def bfs(v):
    dq = deque([])
    visit = [0 for _ in range(n + 1)]
    dq.append(v)
    visit[v] = 1
    while dq:
        node = dq.popleft()
        print(node, end=" ")
        for new_node in lst[node]:
            if visit[new_node] == 0:
                visit[new_node] = 1
                dq.append(new_node)


n, m, v = map(int, input().split())
lst = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for s in lst:
    s.sort()
dfs_visit = [0 for _ in range(n + 1)]
dfs(v)
print()
bfs(v)