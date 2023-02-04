from collections import deque


def chk_range(x, y):
    return True if 0 <= x < N and 0 <= y < N else False


def chk_island(init_x, init_y):
    dq = deque([[init_x, init_y]])
    visit[init_x][init_y] = True
    lst[init_x][init_y] = cnt
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if chk_range(nx, ny) and not visit[nx][ny] and lst[nx][ny] != 0:
                visit[nx][ny] = True
                dq.append([nx, ny])
                lst[nx][ny] = cnt


def bfs(v):
    tmp = 10001
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    dq = deque()

    for i in range(N):
        for j in range(N):
            if lst[i][j] == v:
                dq.append([i, j])
                dist[i][j] = 0

    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if chk_range(nx, ny):
                if lst[nx][ny] > 0 and lst[nx][ny] != v:
                    tmp = min(tmp, dist[x][y])
                    return tmp

                if lst[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append([nx, ny])


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cnt = 1
res = 10001

for i in range(N):
    for j in range(N):
        if lst[i][j] != 0 and not visit[i][j]:
            chk_island(i, j)
            cnt += 1

for i in range(1, cnt):
    res = min(res, bfs(i))
print(res)