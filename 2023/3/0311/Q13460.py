from collections import deque


def move(i, j, dx, dy):
    c = 0
    while lst[i + dx][j + dy] != "#" and lst[i][j] != "O":
        i += dx
        j += dy
        c += 1
    return i, j, c


def bfs():
    while dq:
        rx, ry, bx, by, d = dq.popleft()
        if d > 10:
            break
        for dx, dy in direction:
            nrx, nry, rc = move(rx, ry, dx, dy)
            nbx, nby, bc = move(bx, by, dx, dy)
            if lst[nbx][nby] != "O":
                if lst[nrx][nry] == "O":
                    print(d)
                    return

                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy
                if not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby] = True
                    dq.append([nrx, nry, nbx, nby, d + 1])
    print(-1)


N, M = map(int, input().split())
lst = []
visit = [[[[False for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
red, blue = [], []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(N):
    tmp = list(input().rstrip())
    for j in range(len(tmp)):
        if tmp[j] == "R":
            red = [i, j]
        if tmp[j] == "B":
            blue = [i, j]
    lst.append(tmp)
dq = deque()
dq.append([red[0], red[1], blue[0], blue[1], 1])
visit[red[0]][red[1]][blue[0]][blue[1]] = True
bfs()
