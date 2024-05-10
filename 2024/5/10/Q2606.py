# from collections import deque
#
# def bfs(v):
#     dq = deque([v])
#     visit[v] = 1
#     cnt = 0
#     while dq:
#         x = dq.popleft()
#         for i in lst[x]:
#             if not visit[i]:
#                 cnt += 1
#                 visit[i] = 1
#                 dq.append(i)
#     return cnt


def dfs(v):
    visit[v] = 1
    for i in lst[v]:
        if not visit[i]:
            dfs(i)
            cnt[0] += 1


N = int(input())
M = int(input())
lst = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
cnt = [0]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()
dfs(1)
print(cnt[0])