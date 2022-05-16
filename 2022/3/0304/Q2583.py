from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    cnt = 0
    while dq:
        x, y = dq.popleft()
        for d_x, d_y in direction:
            nx, ny = x + d_x, y + d_y
            if 0 <= nx < M and 0 <= ny < N and not visit[nx][ny] and arr[nx][ny] == 0:
                cnt += 1
                visit[nx][ny] = True
                dq.append([nx, ny])
    if cnt == 0:
        cnt = 1
    return cnt


direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
M, N, K = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(M)]
visit = [[False for _ in range(N)] for _ in range(M)]
res,cnt = [], 0
for _ in range(K):
    ux, uy, dx, dy = map(int, input().split())
    for i in range(uy, dy):
        for j in range(ux, dx):
            arr[i][j] = 1

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0 and not visit[i][j]:
            area = bfs(i, j)
            res.append(area)
            cnt += 1

res.sort()
print(cnt)
for i in res:
    print(i, end=' ')
