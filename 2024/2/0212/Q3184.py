from collections import deque


def bfs(init_x, init_y):
    _o, _v = 0, 0
    visit[init_x][init_y] = True
    dq = deque()
    dq.append([init_x, init_y])
    while dq:
        x, y = dq.popleft()
        if lst[x][y] == 'o':
            _o += 1
        elif lst[x][y] == 'v':
            _v += 1

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and lst[nx][ny] != '#' and visit[nx][ny] == False:
                visit[nx][ny] = True
                dq.append([nx, ny])

    if _o > _v:
        _v = 0
    else:
        _o = 0
    return [_v, _o]


r, c = map(int, input().split())
lst = []
direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
visit = [[False for _ in range(c)] for _ in range(r)]
wolf, sheep = 0, 0
# . 빈 필드, # 울타리, o 양, v 늑대
for _ in range(r):
    lst.append(list(map(str, input().rstrip())))
for i in range(r):
    for j in range(c):
        if visit[i][j] == False and lst[i][j] != '#':
            tmp = bfs(i, j)
            wolf += tmp[0]
            sheep += tmp[1]
print(sheep, wolf)
