import sys
from collections import deque


def bfs(x, y):
    visit = [[-1] * (w + 2) for _ in range(h + 2)]
    dq = deque()
    dq.append([x, y])
    visit[x][y] = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if visit[nx][ny] == -1:
                    if lst[nx][ny] == '.' or lst[nx][ny] == '$':
                        visit[nx][ny] = visit[x][y]
                        dq.appendleft([nx, ny])
                    elif lst[nx][ny] == "#":
                        visit[nx][ny] = visit[x][y] + 1
                        dq.append([nx, ny])
    return visit


direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(int(input())):
    h, w = map(int, input().split())
    lst = [['.'] * (w + 2)]
    prisoner = []
    for i in range(h):
        lst.append(['.'] + list(map(str, input().strip())) + ['.'])  # . : 빈공간, * 벽, # 문, $ 죄수
    lst.append(['.'] * (w + 2))

    for i in range(h + 2):
        for j in range(w + 2):
            if lst[i][j] == "$":
                prisoner.append([i, j])

    one = bfs(prisoner[0][0], prisoner[0][1])
    two = bfs(prisoner[1][0], prisoner[1][1])
    sang = bfs(0, 0)
    ans = sys.maxsize
    for i in range(h + 2):
        for j in range(w + 2):
            if one[i][j] != -1 and two[i][j] != -1 and sang[i][j] != -1:
                res = one[i][j] + two[i][j] + sang[i][j]
                if lst[i][j] == "*":
                    continue
                if lst[i][j] == "#":
                    res -= 2
                ans = min(ans, res)
    print(ans)