from collections import deque


def bfs(x, y):
    cnt = 1
    dq = deque()
    dq.append([x, y])
    visit[x][y] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and paint[nx][ny] == 1 and not visit[nx][ny]:
                dq.append([nx, ny])
                visit[nx][ny] = True
                cnt += 1
    res.append(cnt)


N, M = map(int, input().split())
paint, res = [], []
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visit = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    paint.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        if paint[i][j] == 1 and not visit[i][j]:
            bfs(i, j)
if res:
    print(len(res))
    print(max(res))
else:
    print(0)
    print(0)