from collections import deque


def bfs(start, end):
    dq = deque()
    dq.append(start)
    visit = [-1] * (N + 1)
    visit[start] = 0
    while dq:
        x = dq.popleft()
        if x == end:
            break
        for adj_node, adj_dist in lst[x]:
            if visit[adj_node] > -1:
                continue
            visit[adj_node] = visit[x] + adj_dist
            dq.append(adj_node)
    return visit[end]


inf = 10 ** 10
N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
for _ in range(M):
    s, e = map(int, input().split())
    print(bfs(s, e))
