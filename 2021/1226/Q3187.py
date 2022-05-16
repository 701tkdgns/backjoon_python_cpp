def bfs(x, y):
    global w, k
    visit[x][y] = 1
    queue.append([x, y])
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]
        if lst[x][y] == 'v':
            w += 1
        elif lst[x][y] == 'k':
            k += 1
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and lst[nx][ny] != '#' and visit[nx][ny] == 0:
                queue.append((nx, ny))
                visit[nx][ny] = 1


R, C = map(int, input().split())
lst = [[''] * C for _ in range(R)]
visit = [[0] * C for _ in range(R)]
queue = []
wolf, sheep = 0, 0
for i in range(R):
    lst[i] = list(input().rstrip())
for i in range(R):
    for j in range(C):
        if lst[i][j] != '#' and visit[i][j] == 0:
            w, k = 0, 0
            bfs(i, j)
            if w >= k:
                k = 0
            else:
                w = 0
            wolf += w
            sheep += k
print(sheep, wolf)
