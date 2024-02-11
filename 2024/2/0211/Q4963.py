from collections import deque


def bfs(init_x, init_y):
    dq = deque()
    dq.append([init_x, init_y])
    visit[init_x][init_y] = 1
    while dq:
        x, y = dq.popleft()
        for dx, dy in pos:
            nx, ny = dx + x, dy + y
            if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == 0 and lst[nx][ny] == 1:
                dq.append([nx, ny])
                visit[nx][ny] = 1


pos = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    lst = []
    visit = [[0 for _ in range(w)] for _ in range(h)]
    for _ in range(h):
        _lst = list(map(int, input().split()))
        lst.append(_lst)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and lst[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)
