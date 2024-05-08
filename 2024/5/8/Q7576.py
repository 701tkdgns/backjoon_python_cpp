from collections import deque


def tomato():
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                visit[i][j] = 0
                dq.append([i, j])
            elif lst[i][j] == -1:
                visit[i][j] = -2


def bfs():
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == -1 and lst[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                dq.append([nx, ny])


M, N = map(int, input().split())
visit = [[-1 for _ in range(M)] for _ in range(N)]
lst = [list(map(int, input().split())) for _ in range(N)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dq = deque([])
res = 0
tomato()
bfs()
for i in visit:
    if -1 in i:
        res = -1
        break
    else:
        res = max(res, max(i))
print(res)