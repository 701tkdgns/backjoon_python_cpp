from collections import deque


def bfs(init_x, init_y, ex, ey):
    dq = deque([[init_x, init_y]])
    visit[init_x][init_y] = 0
    while dq:
        x, y = dq.popleft()
        if x == ex and y == ey:
            break
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == -1:
                dq.append([nx, ny])
                visit[nx][ny] = visit[x][y] + 1


T = int(input())
direction = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
for _ in range(T):
    n = int(input())
    lst = [[0 for _ in range(n)] for _ in range(n)]
    visit = [[-1 for _ in range(n)] for _ in range(n)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    bfs(start_x, start_y, end_x, end_y)
    print(visit[end_x][end_y])