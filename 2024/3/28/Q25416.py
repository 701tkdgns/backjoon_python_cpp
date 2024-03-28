from collections import deque

def bfs(_x, _y):
    dq = deque([[_x, _y]])
    visit[_x][_y] = 0
    while dq:
        x, y = dq.popleft()
        if lst[x][y] == 1:
            return visit[x][y]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0<= nx< 5 and 0 <= ny < 5 and visit[nx][ny] == -1 and  lst[nx][ny] != -1:
                visit[nx][ny] = visit[x][y] + 1
                dq.append([nx, ny])
    return -1

lst = []
visit = [[-1 for _ in range(5)] for _ in range(5)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(5):
    lst.append(list(map(int, input().split())))
i, j = map(int, input().split())
res = bfs(i, j)
print(res)