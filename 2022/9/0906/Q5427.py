import sys
from collections import deque

std = sys.stdin.readline
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def is_valid_coord(x, y):
    return 0 <= x < h and 0 <= y < w


def fire():
    for _ in range(len(fq)):
        x, y = fq.popleft()
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if is_valid_coord(nx, ny) and lst[nx][ny] == '.':
                lst[nx][ny] = '*'
                fq.append([nx, ny])


def move(x, y):
    visit[x][y] = 1
    dq.append([x, y])
    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if is_valid_coord(nx, ny) and visit[nx][ny] == 0 and lst[nx][ny] == '.':
                    dq.append([nx, ny])
                    visit[nx][ny] = visit[x][y] + 1
                if not is_valid_coord(nx, ny):
                    print(visit[x][y])
                    return
        fire()
    print("IMPOSSIBLE")
    return


for _ in range(int(std())):
    w, h = map(int, std().split())
    lst = [list(map(str, std().rstrip())) for _ in range(h)]
    visit = [[0] * w for _ in range(h)]
    fq, dq = deque(), deque()
    sx, sy = 0, 0
    for i in range(h):
        for j in range(w):
            if lst[i][j] == '@':
                sx, sy = i, j
                lst[i][j] = '.'
            if lst[i][j] == '*':
                fq.append([i, j])
    fire()
    move(sx, sy)

# import sys
# from collections import deque
#
# input = sys.stdin.readline
# dx = (1, 0, -1, 0)
# dy = (0, 1, 0, -1)
#
#
# def is_valid_coord(y, x):
#     return 0 <= y < N and 0 <= x < M
#
#
# def fire():
#     for _ in range(len(fq)):
#         y, x = fq.popleft()
#         for k in range(4):
#             ny = y + dy[k]
#             nx = x + dx[k]
#             if (0 <= ny < N and 0 <= nx < M) and board[ny][nx] == ".":
#                 board[ny][nx] = "*"
#                 fq.append((ny, nx))
#
#
# def moving(y, x):
#     visited[y][x] = 1
#     dq.append((y, x))
#     while dq:
#         for _ in range(len(dq)):
#             y, x = dq.popleft()
#             for k in range(4):
#                 ny = y + dy[k]
#                 nx = x + dx[k]
#                 if is_valid_coord(ny, nx) and visited[ny][nx] == 0 and board[ny][nx] == ".":
#                     dq.append((ny, nx))
#                     visited[ny][nx] = visited[y][x] + 1
#                 if not is_valid_coord(ny, nx):
#                     print(visited[y][x])
#                     return
#         fire()
#
#     print("IMPOSSIBLE")
#     return
#
#
# T = int(input())
# for _ in range(T):
#     M, N = map(int, input().split())
#     board = [list(map(str, input().rstrip())) for _ in range(N)]
#     visited = [[0] * M for _ in range(N)]
#     fq = deque()
#     dq = deque()
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == "@":
#                 sy, sx = i, j
#                 board[i][j] = "."
#             if board[i][j] == "*":
#                 fq.append((i, j))
#     fire()
#     moving(sy, sx)
