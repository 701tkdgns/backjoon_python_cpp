import sys
from collections import deque

std = sys.stdin.readline
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def R(x, y):
    dq = deque()
    dq.append([x, y])
    visit[x][y] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and lst[nx][ny] == 'R':
                dq.append([nx, ny])
                visit[nx][ny] = True


def G(x, y):
    dq = deque()
    dq.append([x, y])
    visit[x][y] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and lst[nx][ny] == 'G':
                dq.append([nx, ny])
                visit[nx][ny] = True


def B(x, y):
    dq = deque()
    dq.append([x, y])
    visit[x][y] = True
    c = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and lst[nx][ny] == 'B':
                dq.append([nx, ny])
                visit[nx][ny] = True


def RG(x, y):
    dq = deque()
    dq.append([x, y])
    visit_rg[x][y] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit_rg[nx][ny] and (lst[nx][ny] == 'R' or lst[nx][ny] == 'G'):
                dq.append([nx, ny])
                visit_rg[nx][ny] = True


def RGB(x, y):
    dq = deque()
    dq.append([x, y])
    visit_rg[x][y] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit_rg[nx][ny] and lst[nx][ny] == 'B':
                dq.append([nx, ny])
                visit_rg[nx][ny] = True


N = int(std())
lst = []
for _ in range(N):
    lst.append(list(map(str, std().rstrip())))
visit = [[False for _ in range(N)] for _ in range(N)]
visit_rg = [[False for _ in range(N)] for _ in range(N)]
cnt, rg = 0, 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 'R' and not visit[i][j]:
            R(i, j)
            cnt += 1
        elif lst[i][j] == 'G' and not visit[i][j]:
            G(i, j)
            cnt += 1
        elif lst[i][j] == 'B' and not visit[i][j]:
            B(i, j)
            cnt += 1

        if (lst[i][j] == 'R' or lst[i][j] == 'G') and not visit_rg[i][j]:
            RG(i, j)
            rg += 1
        elif lst[i][j] == 'B' and not visit_rg[i][j]:
            RGB(i, j)
            rg += 1
print(cnt, rg)
