from collections import deque


def bfs():
    while dq:
        x, y = dq.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and lst[nx][ny] == 0:
                lst[nx][ny] = lst[x][y] + 1
                dq.append([nx, ny])


N, M = map(int, input().split())
lst = []
dq = deque()
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = 0
for i in range(M):
    tmp = list(map(int, input().split()))
    if 1 in tmp:
        dq.append([i, tmp.index(1)])
    lst.append(tmp)
bfs()
for i in lst:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)