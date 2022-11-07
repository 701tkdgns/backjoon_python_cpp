from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and lst[x][y] == 1 and visit[nx][ny] == 0:
                if lst[nx][ny] == 1:
                    dq.append([nx, ny])
                    visit[nx][ny] = 1
                if lst[nx][ny] == 0:
                    visit[nx][ny] = 1
                    lst[x][y] = 0


N, M = map(int, input().split())
lst = []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(N):
    lst.append(list(map(int, input().split())))
visit = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1 and visit[i][j] == 0:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        print(lst[i][j], end=" ")
    print()
