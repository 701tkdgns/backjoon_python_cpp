from collections import deque


def bfs(_x, _y):
    dq = deque([[_x, _y]])
    visit[_x][_y] = 1

    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 and graph[nx][ny] == 255:
                visit[nx][ny] = 1
                dq.append([nx, ny])


N, M = map(int, input().split())
lst, graph = [], [[] for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
r, g, b = [], [], []
res = 0
for i in range(N):
    lst.append(list(map(int, input().split())))
T = int(input())
for i in range(N):
    for j in range(0, M * 3, 3):
        if sum(lst[i][j:j+3]) / 3 >= T:
            graph[i].append(255)
        else:
            graph[i].append(0)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 255 and visit[i][j] == 0:
            bfs(i, j)
            res += 1
print(res)
