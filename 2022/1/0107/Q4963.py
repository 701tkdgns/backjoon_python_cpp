def bfs(x, y):
    global cnt
    queue.append([x, y])
    direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    visit[x][y] = True
    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]
        if lst[x][y] == 1:
            cnt = 1
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and lst[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append([nx, ny])


while True:
    queue = []
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    lst = [[] * w for _ in range(h)]
    visit = [[False] * w for _ in range(h)]
    for i in range(h):
        lst[i] = list(map(int, input().split()))
    cnt, res = 0, 0
    for i in range(h):
        for j in range(w):
            if lst[i][j] == 1 and not visit[i][j]:
                bfs(i, j)
                res += cnt
    print(res)
