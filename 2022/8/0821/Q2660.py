from collections import deque


def bfs(v):
    dq = deque([v])
    visit[v] = 0
    while dq:
        new_v = dq.popleft()
        for idx in lst[new_v]:
            if visit[idx] == -1:
                visit[idx] = visit[new_v] + 1
                dp[v] = visit[idx]
                dq.append(idx)


N = int(input())
lst = [[] for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()
for i in range(1, N + 1):
    visit = [-1 for _ in range(N + 1)]
    bfs(i)
score, cnt = min(dp[1:]), 0
res = []
for i in range(1, N + 1):
    if dp[i] == score:
        cnt += 1
        res.append(i)
print(score, cnt)
print(*res)
