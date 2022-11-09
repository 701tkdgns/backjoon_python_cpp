from collections import deque


def bfs(x, y, z):
    dq = deque()
    dq.append([x, y, z])
    while dq:
        x, y, z = dq.popleft()
        if x == N - 1 and y == M - 1:
            return visit[x][y][z]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if lst[nx][ny] == 2 and z == 0:
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    dq.append([nx, ny, 1])
                elif z == 1 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    dq.append([nx, ny, z])
                elif lst[nx][ny] == 0 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    dq.append([nx, ny, z])


direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M, T = map(int, input().split())
lst = []
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    lst.append(list(map(int, input().split())))
res = bfs(0, 0, 0)
if res is None or res > T:
    print("Fail")
else:
    print(res)
