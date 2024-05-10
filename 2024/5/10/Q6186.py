from collections import deque


def bfs(X, Y):
    dq = deque([[X, Y]])
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and lst[nx][ny] == '#' and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dq.append([nx, ny])


R, C = map(int, input().split())
lst = [list(map(str, input().rstrip())) for _ in range(R)]
visit = [[0 for _ in range(C)] for _ in range(R)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cnt = 0

for i in range(R):
    for j in range(C):
        if lst[i][j] == '#' and visit[i][j] == 0:
            visit[i][j] = 1
            bfs(i, j)
            cnt += 1
print(cnt)