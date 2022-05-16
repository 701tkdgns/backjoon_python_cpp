from collections import deque


def bfs(i, j):
    dq = deque()
    dq.append([i, j])
    chk[i][j] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if 0 <= nx < h and 0 <= ny < w and not chk[nx][ny] and lst[nx][ny] == 1:
                chk[nx][ny] = True
                dq.append([nx, ny])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    lst = []
    chk = [[False for _ in range(w)] for _ in range(h)]
    direction = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for _ in range(h):
        L = list(map(int, input().split()))
        lst.append(L)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if not chk[i][j] and lst[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)