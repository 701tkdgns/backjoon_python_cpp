def bfs(x, y):
    global res
    queue = [[x, y]]
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]
        if fence[x][y] == 'W':
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and fence[nx][ny] == 'S':
                    res = 0
                    return
                elif 0 <= nx < R and 0 <= ny < C and not visit[nx][ny] and fence[nx][ny] != 'W' and fence[nx][ny] != 'S':
                    fence[nx][ny] = 'D'
                    visit[nx][ny] = True
        else:
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not visit[nx][ny] and fence[nx][ny] == '.':
                    fence[nx][ny] = 'D'
                    visit[nx][ny] = True
                    queue.append([nx, ny])


R, C = map(int, input().split())
fence = [['' for _ in range(C)] for _ in range(R)]
visit = [[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    fence[i] = list(input().rstrip())
res = 1
for i in range(R):
    for j in range(C):
        if not visit[i][j]:
            bfs(i, j)

if res == 1:
    print(res)
    for i in fence:
        for j in i:
            print(j, end='')
        print()
else:
    print(res)