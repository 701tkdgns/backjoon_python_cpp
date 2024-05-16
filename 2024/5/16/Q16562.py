from collections import deque


def bfs(X):
    dq = deque([X])
    m = 10001
    while dq:
        x = dq.popleft()
        for i in lst[x]:
            if visit[i] == 0:
                m = min(m, N[i], N[X])
                visit[i] = 1
    print(X, m)
    return m


n, m, k = map(int, input().split())
N = list(map(int, input().split()))
lst = [[] for _ in range(n)]
visit = [0 for _ in range(n)]
cnt = 0
for _ in range(m):
    v, w = map(int, input().split())
    lst[v - 1].append(w - 1)
    lst[w - 1].append(v - 1)
for i in range(n):
    if visit[i] == 0:
        visit[i] = 1
        cnt += bfs(i)
print(cnt)