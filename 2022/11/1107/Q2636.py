from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    visit[x][y] = 1
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and lst[x][y] == 0 and visit[nx][ny] == 0:
                if lst[nx][ny] == 1:
                    visit[nx][ny] = 1
                    lst[nx][ny] = 0
                else:
                    visit[nx][ny] = 1
                    dq.append([nx, ny])


N, M = map(int, input().split())
lst = []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(N):
    lst.append(list(map(int, input().split())))


tmp = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            tmp += 1
res, time = tmp, 0
for t in range(1, 10001):
    visit = [[0 for _ in range(M)] for _ in range(N)]
    bfs(0, 0)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                cnt += 1
    if cnt == 0:
        res, time = tmp, t
        break
    else:
        tmp = cnt
print(time)
print(res)
