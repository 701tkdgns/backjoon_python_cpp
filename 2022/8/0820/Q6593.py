from collections import deque
direction = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]


def bfs(x, y, z):
    dq = deque()
    dq.append([x, y, z])
    visit[x][y][z] = 0
    while dq:
        x, y, z = dq.popleft()
        for dx, dy, dz in direction:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C and visit[nx][ny][nz] == -1:
                if lst[nx][ny][nz] == '.':
                    dq.append([nx, ny, nz])
                    visit[nx][ny][nz] = visit[x][y][z] + 1
                elif lst[nx][ny][nz] == 'E':
                    visit[nx][ny][nz] = visit[x][y][z] + 1
                    return


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    lst = [[['' for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visit = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    start_x, start_y, start_z = 0, 0, 0
    end_x, end_y, end_z = 0, 0, 0
    for i in range(L):
        for j in range(R):
            tmp = input()
            for t in range(len(tmp)):
                lst[i][j][t] = tmp[t]
                if lst[i][j][t] == 'S':
                    start_x, start_y, start_z = i, j, t
                if lst[i][j][t] == 'E':
                    end_x, end_y, end_z = i, j, t
        input()
    bfs(start_x, start_y, start_z)
    if visit[end_x][end_y][end_z] != -1:
        print("Escaped in {} minute(s).".format(visit[end_x][end_y][end_z]))
    else:
        print("Trapped!")
