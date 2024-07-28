from collections import deque


def bfs(init_x, init_y, init_d):
    cnt = 0
    dq = deque([])
    dq.append([init_x, init_y, init_d])
    while dq:
        x, y, d = dq.popleft()
        if graph[x][y] == 0:
            cnt += 1
            graph[x][y] = 2
            dq.append([x, y, d])
        else:
            chk = False
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    chk = True
                    break
            if not chk:
                tmp_d = (d + 2) % 4
                nx, ny = x + directions[tmp_d][0], y + directions[tmp_d][1]
                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] != 1:
                        dq.append([nx, ny, d])
                    else:
                        return cnt
            else:
                for _ in range(4):
                    d = d - 1 if d - 1 >= 0 else 3
                    nx, ny = x + directions[d][0], y + directions[d][1]
                    if 0 <= nx < N and 0 <= ny < M:
                        if graph[nx][ny] == 0:
                            dq.append([nx, ny, d])
                            break


N, M = map(int, input().split())
R, C, D = map(int, input().split())
graph = []
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
res = bfs(R, C, D)
print(res)
