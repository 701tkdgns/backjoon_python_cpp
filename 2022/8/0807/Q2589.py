from collections import deque
import sys


def bfs(x, y):
    mx = 0
    dq = deque()
    dq.append([x, y])
    visit[x][y] = 1
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if 0 <= nx < L and 0 <= ny < W and visit[nx][ny] == 0 and lst[nx][ny] != 'W':
                visit[nx][ny] = 1
                lst[nx][ny] = lst[x][y] + 1
                mx = max(lst[nx][ny], mx)
                dq.append([nx, ny])
    return mx


std = sys.stdin
L, W = map(int, std.readline().split())
lst = []
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = 0
for _ in range(L):
    lst.append(list(map(str, std.readline().rstrip())))
for i in range(L):
    for j in range(W):
        if lst[i][j] != 'W':
            visit = [[0 for _ in range(W)] for _ in range(L)]
            lst[i][j] = 0
            res = max(res, bfs(i, j))
print(res)