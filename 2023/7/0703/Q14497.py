from collections import deque

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
lst = [list(map(str, input().rstrip())) for _ in range(N)]
visit = [[-1 for _ in range(M)] for _ in range(N)]
dq = deque([])
visit[x1 - 1][y1 - 1] = 0
dq.append([x1 - 1, y1 - 1])
while dq:
    x, y = dq.popleft()
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == -1:
            if lst[nx][ny] == "1" or lst[nx][ny] == "#":
                visit[nx][ny] = visit[x][y] + 1
                dq.append([nx, ny])
            elif lst[nx][ny] == "0":
                visit[nx][ny] = visit[x][y]
                dq.appendleft([nx, ny])
print(visit[x2 - 1][y2 - 1])
