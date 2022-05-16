from collections import deque

def dfs(v):
    dq = deque([v])
    while dq:
        v = dq.popleft()
        for i in adj[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                dq.append(i)



N = int(input())
i, j = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for line in adj:
    line.sort()

dfs(i)
print(visited[j])























# from collections import deque
#
#
# def bfs(v):
#     dq = deque([v])
#     while dq:
#         v = dq.popleft()
#         for idx in adj[v]:
#             if visited[idx] == 0:
#                 visited[idx] = visited[v] + 1
#                 dq.append(idx)
#
# N = int(input())
# a, b = map(int, input().split())
# M = int(input())
# visited = [0] * (N+1)
# adj = [[] for _ in range(N+1)]
# for _ in range(M):
#     i, j = map(int, input().split())
#     adj[i].append(j)
#     adj[j].append(i)
#
# for lst in adj:
#     lst.sort()
# bfs(a)
# print(visited[b] if visited[b] > 0 else -1)