import copy
from collections import deque


def bfs():
    global res
    dq = deque()
    visit = copy.deepcopy(lst)
    tmp = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 2:
                dq.append([i, j])
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                visit[nx][ny] = 2
                dq.append([nx, ny])

    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                tmp += 1
    res = max(res, tmp)

def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 0:
                lst[i][j] = 1
                wall(cnt + 1)
                lst[i][j] = 0

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
res = 0
wall(0)
print(res)