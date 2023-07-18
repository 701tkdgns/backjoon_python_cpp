from collections import deque


def delete(_tmp):
    for x, y in _tmp:
        lst[x][y] = "."


def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if lst[j][i] != "." and lst[k][i] == ".":
                    lst[k][i] = lst[j][i]
                    lst[j][i] = "."
                    break


def bfs(x, y):
    dq = deque([[x, y]])
    now = lst[x][y]
    visit[x][y] = 1
    tmp.append([x, y])

    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 12 and 0 <= ny < 6 and lst[nx][ny] == now and not visit[nx][ny]:
                visit[nx][ny] = 1
                dq.append([nx, ny])
                tmp.append([nx, ny])


lst = [list(map(str, input().rstrip())) for _ in range(12)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = 0

while True:
    visit = [[0 for _ in range(6)] for _ in range(12)]
    chk = 0

    for i in range(12):
        for j in range(6):
            if lst[i][j] != "." and not visit[i][j]:
                tmp = []
                bfs(i, j)
                if len(tmp) >= 4:
                    chk = 1
                    delete(tmp)
    if not chk:
        break
    down()
    res += 1
print(res)
