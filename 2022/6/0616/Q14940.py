from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    res[x][y] = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and lst[nx][ny]:
                res[nx][ny] = res[x][y] + 1
                dq.append([nx, ny])
                visit[nx][ny] = True


N, M = map(int, input().split())
rx, ry = 0, 0
lst = []
res = [[-1 for _ in range(M)] for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(N):
    tmp = list(map(int, input().split()))
    lst.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 2:
            rx, ry = i, j
            visit[rx][ry] = True

for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            res[i][j] = 0

bfs(rx, ry)

for v in res:
    print(*v)