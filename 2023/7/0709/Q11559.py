from collections import deque


def check(x, y):
    dq = deque([[x, y]])
    now = lst[x][y]
    pos = []
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 12 and 0 <= ny < 6 and lst[nx][ny] == now and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                pos.append([x, y])
                dq.append([nx, ny])

    pos.sort(key=lambda x: (x[1], x[0]))
    for i, j in pos:
        lst[i][j] = "_"
        bombList.append([i, j])


lst = [list(map(str, input().rstrip())) for _ in range(12)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = 0
while True:
    visit = [[0 for _ in range(6)] for _ in range(12)]
    bombList = []
    for i in range(12):
        for j in range(6):
            if lst[i][j] != "." and lst[i][j] != "_" and visit[i][j] == 0:
                check(i, j)
    if len(bombList) == 0:
        break

    for bomb in bombList:
        x, y = bomb[0], bomb[1]
        for i in range(x, 0, -1):
            lst[i][y] = lst[i - 1][y]
        lst[0][y] = "."
    res += 1


# from collections import deque
#
#
# def check(x, y):
#     dq = deque([x, y])
#     now = lst[x][y]
#     pos = []
#     while dq:
#         x, y = dq.popleft()
#         for dx, dy in direction:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < 12 and 0 <= ny < 6 and lst[nx][ny] == now and not visit[nx][ny]:
#                 pos.append([nx, ny])
#                 dq.append([nx, ny])
#                 visit[nx][ny] = 1
#     if len(pos) >= 4:
#         pos.sort(key=lambda x: (x[1], x[0]))
#         for i, j in pos:
#             lst[i][j] = "_"
#             bombList.append([i, j])
#
#
# lst = [list(map(str, input().rstrip())) for _ in range(12)]
# direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# res = 0
# while True:
#     visit = [[0] * 6 for _ in range(12)]
#     bombList = []
#     for i in range(12):
#         for j in range(6):
#             if lst[i][j] != "." and lst[i][j] != "_" and not visit[i][j]:
#                 check(i, j)
#
#     if len(bombList) == 0:
#         break
#
#     for bomb in bombList:
#         x, y = bomb[0], bomb[1]
#         for i in range(x, 0, -1):
#             lst[i][y] = lst[i - 1][y]
#         lst[0][y] = "."
#     res += 1
# print(res)

from collections import deque

def check(x, y):
    dq = deque([x, y])
    now = lst[x][y]
    pos = []
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 12 and 0 <= ny < 6 and lst[nx][ny] == now and not visit[nx][ny]:
                pos.append([nx, ny])
                dq.append([nx, ny])
                visit[nx][ny] = 1
    if len(pos) >= 4:
        pos.sort(key=lambda x:(x[1], x[0]))
        for i, j in pos:
            lst[i][j] = "_"
            bomblist.append([i, j])


lst = [list(map(str, input().rstrip())) for _ in range(12)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = 0
while True:
    visit = [[0 for _ in range(6)] for _ in range(12)]
    bomblist = []
    for i in range(12):
        for j in range(6):
            if lst[i][j] != "." and lst[i][j] != "_" and not visit[i][j]:
                check(i, j)

    if len(bomblist) == 0:
        break

    for bomb in bomblist:
        x, y = bomb[0], bomb[1]
        for i in range(x, 0, -1):
            lst[i][y] = lst[i - 1][y]
        lst[0][y]= "."
    res += 1