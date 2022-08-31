from collections import deque


def bfs():
    while dq:
        x, y, z = dq.popleft()
        for dx, dy, dz in direction:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < H and 0 <= ny < M and 0 <= nz < N and lst[nx][ny][nz] == 0:
                lst[nx][ny][nz] = lst[x][y][z] + 1
                dq.append([nx, ny, nz])


N, M, H = map(int, input().split())
lst = []
dq = deque()
direction = [(0, 0, 1), (0, 0, -1), (-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0)]
for i in range(H):
    tmp = []
    for j in range(M):
        tmp_r = list(map(int, input().split()))
        tmp.append(tmp_r)
    lst.append(tmp)
for i in range(H):
    for j in range(M):
        for k in range(N):
            if lst[i][j][k] == 1:
                dq.append([i, j, k])

bfs()
res = 0
for i in range(H):
    for j in range(M):
        for k in range(N):
            if lst[i][j][k] == 0:
                print(-1)
                exit(0)
            elif res < lst[i][j][k]:
                res = lst[i][j][k]
print(res-1)
