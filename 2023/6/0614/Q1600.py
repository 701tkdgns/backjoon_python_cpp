from collections import deque


def bfs():
    visit[0][0][0] = 1
    dq = deque([[0, 0, 0]])
    while dq:
        x, y, z = dq.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][z] - 1

        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if (0 <= nx < n and 0 <= ny < m) and visit[nx][ny][z] == 0 and lst[nx][ny] == 0:
                visit[nx][ny][z] = visit[x][y][z] + 1
                dq.append([nx, ny, z])

        if z < K:
            for dx, dy in horse_d:
                hx, hy = dx + x, dy + y
                if (0 <= hx < n and 0 <= hy < m) and visit[hx][hy][z + 1] == 0 and lst[hx][hy] == 0:
                    visit[hx][hy][z + 1] = visit[x][y][z] + 1
                    dq.append([hx, hy, z + 1])
    return -1


K = int(input())
m, n = map(int, input().split())
lst = []
visit = [[[0] * (K + 1) for _ in range(m)] for _ in range(n)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
horse_d = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
for _ in range(n):
    lst.append(list(map(int, input().split())))
print(bfs())