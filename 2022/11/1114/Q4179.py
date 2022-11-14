from collections import deque


def fire():
    while fq:
        x, y = fq.popleft()
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if 0 <= nx < r and 0 <= ny < c and lst[nx][ny] == '.':
                lst[nx][ny] = "F"
                fq.append([nx, ny])


def bfs(init_x, init_y):
    visit[init_x][init_y] = 1
    dq.append([init_x, init_y])
    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    if visit[nx][ny] == 0 and lst[nx][ny] == '.':
                        dq.append([nx, ny])
                        visit[nx][ny] = visit[x][y] + 1
                else:
                    print(visit[x][y])
                    return
        fire()
    print("IMPOSSIBLE")
    return


r, c = map(int, input().split())
lst = []
visit = [[0 for _ in range(c)] for _ in range(r)]
J, F = [], []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(r):
    lst.append(list(map(str, input().rstrip())))
    for j in lst[i]:
        if j == "J":
            J = [i, lst[i].index("J")]
            lst[J[0]][J[1]] = '.'
        if j == "F":
            F = [i, lst[i].index("F")]
dq, fq = deque(), deque()
fq.append([F[0], F[1]])
fire()
bfs(J[0], J[1])
