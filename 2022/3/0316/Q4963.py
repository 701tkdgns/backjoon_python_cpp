from collections import deque
direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    visit[x][y] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and lst[nx][ny] and not visit[nx][ny]:
                dq.append([nx, ny])
                visit[nx][ny] = True
    return 1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    lst = []
    visit = [[False for _ in range(w)] for _ in range(h)]
    cnt = 0
    for i in range(h):
        lst.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if lst[i][j] == 1 and not visit[i][j]:
                tmp = bfs(i, j)
                cnt += tmp
    print(cnt)
