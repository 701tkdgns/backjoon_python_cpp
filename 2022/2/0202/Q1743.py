from collections import deque


def bfs(x, y):
    global cnt
    dq = deque()
    dq.append((x, y))
    visit[x][y] = True
    while dq:
        x, y = dq.popleft()
        cnt += 1
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N and 0 <= ny <= M and lst[nx][ny] == 1 and not visit[nx][ny]:
                dq.append([nx, ny])
                visit[nx][ny] = True


N, M, K = map(int, input().split())
lst = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
visit = [[False for _ in range(M + 1)] for _ in range(N + 1)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = 0
for i in range(K):
    a, b = map(int, input().split())
    lst[a][b] = 1

for i in range(1, N + 1):
    for j in range(1, M + 1):
        cnt = 0
        if lst[i][j] == 1 and not visit[i][j]:
            bfs(i, j)
        res = max(cnt, res)
print(res)