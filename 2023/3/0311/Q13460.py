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
                    return d

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
    return -1


N, M = map(int, input().split())
lst = []
visit = [[[[False for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)]
_rx, _ry, _bx, _by = 0, 0, 0, 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(N):
    tmp = list(input().rstrip())
    for j in range(len(tmp)):
        if tmp[j] == "R":
            _rx, _ry = i, j
        if tmp[j] == "B":
            _bx, _by = i, j
    lst.append(tmp)
dq = deque()
dq.append([_rx, _ry, _bx, _by, 1])
visit[_rx][_ry][_bx][_by] = True
res = bfs()
print(res)