from collections import deque


def bfs(v):
    dq = deque([v])
    visit[v] = 1
    cnt = 2
    while dq:
        v = dq.popleft()
        for i in lst[v]:
            if visit[i] == 0:
                visit[i] = cnt
                dq.append(i)
                cnt += 1


N, M, R = map(int, input().split())
lst = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
cnt = 1
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for e in lst:
    e.sort()
bfs(R)
for i in range(1, N + 1):
    print(visit[i])