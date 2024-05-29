<<<<<<< Updated upstream
from collections import deque


def bfs(init_x, init_y, init_d):
    dq = deque([])
    dq.append([init_x, init_y, init_d])
    cnt = 0
    while dq:
        x, y, d = dq.popleft()
        if graph[x][y] == 0:
            graph[x][y] = 2
            cnt += 1
            # dq.append([x, y, d])
            # else:
        chk = False
        idx = 0
        for dir_idx in range(len(direction) + d - 1, d - 1, -1):
            nx, ny = direction[dir_idx % 4][0] + x, direction[dir_idx % 4][1] + y
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                idx = dir_idx
                chk = True
                break
        if chk:
            dq.append([nx, ny, idx])
        else:
            nx, ny = direction[(d + 2) % 4][0] + x, direction[(d + 2) % 4][1] + y
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 1:
                dq.append([nx, ny, d])
            else:
                break
    return cnt

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = map(int, input().split())
R, C, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
res = bfs(R, C, D)
print(res)
=======
N, M = map(int, input().split())
R, C, D = map(int, input().split())
>>>>>>> Stashed changes
