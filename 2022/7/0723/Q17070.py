from collections import deque


def bfs():
    visit[0][0] = True
    visit[0][1] = True
    cnt = 0
    dq = deque([[0, 1]])
    tmp = [[0, 0], [0, 1]]
    direction_o = [(1, 0), (1, 1)]
    direction_w = [(0, 1), (1, 1)]
    direction_t = [(1, 0), (0, 1), (1, 1)]
    while dq:
        x, y = tmp[0]
        i, j = tmp[1]
        del tmp[0], tmp[1]
        x, y = abs(x - i), abs(y - j)
        if x == 1 and y == 0:
            for dx, dy in direction_o:
                nx, ny = x + dx, y + dy
        elif x == 0 and y == 1:
            for dx, dy in direction_w:
                nx, ny = x + dx, y + dy
        elif x == 1 and y == 1:
            for dx, dy in direction_t:
                nx, ny = x + dx, y + dy


N = int(input())
lst = []
visit = [[False] * N for _ in range(N)]
for _ in range(N):
    lst.append(list(map(int, input().split())))
