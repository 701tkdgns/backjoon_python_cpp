# import sys
# from collections import deque
# std = sys.stdin
#
#
# def bfs(x1, y1, x2, y2):
#     dq = deque()
#     dq.append([x1, y1, x2, y2])
#     cnt = 0
#     while dq:
#         x1, y1, x2, y2 = dq.popleft()
#         if x2 == N - 1 and y2 == N - 1:
#             cnt += 1
#         x, y = x2 - x1, y2 - y1
#         if x == 1 and y == 0:
#             for dx, dy in direction_h:
#                 nx, ny = dx + x2, dy + y2
#                 if dx == 1 and dy == 1:
#                     if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 0 and lst[nx - 1][ny] == 0 and lst[nx][ny - 1] == 0:
#                         dq.append([x2, y2, nx, ny])
#                 elif 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 0:
#                     dq.append([x2, y2, nx, ny])
#         elif x == 0 and y == 1:
#             for dx, dy in direction_v:
#                 nx, ny = dx + x2, dy + y2
#                 if dx == 1 and dy == 1:
#                     if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 0 and lst[nx - 1][ny] == 0 and lst[nx][ny - 1] == 0:
#                         dq.append([x2, y2, nx, ny])
#                 elif 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 0:
#                     dq.append([x2, y2, nx, ny])
#         elif x == 1 and y == 1:
#             for dx, dy in direction_c:
#                 nx, ny = dx + x2, dy + y2
#                 if dx == 1 and dy == 1:
#                     if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 0 and lst[nx - 1][ny] == 0 and lst[nx][ny - 1] == 0:
#                         dq.append([x2, y2, nx, ny])
#                 elif 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == 0:
#                     dq.append([x2, y2, nx, ny])
#     print(cnt)
#
#

import sys

std = sys.stdin
sys.setrecursionlimit(10 ** 6)


def dfs(x, y, direction):
    S = 0
    if x == N - 1 and y == N - 1:
        return 1
    if direction == 0 or direction == 2:
        ny = y + 1
        if ny < N and lst[x][ny] == 0:
            S += dfs(x, ny, 0)
    if direction == 1 or direction == 2:
        nx = x + 1
        if nx < N and lst[nx][y] == 0:
            S += dfs(nx, y, 1)
    nx, ny = x + 1, y + 1
    if nx < N and ny < N and lst[nx][ny] == 0 and lst[nx - 1][ny] == 0 and lst[nx][ny - 1] == 0:
        S += dfs(nx, ny, 2)
    return S


N = int(std.readline().strip())
lst = []
for _ in range(N):
    lst.append(list(map(int, std.readline().strip().split())))
if lst[N - 1][N - 1] == 1 or lst[0][2] == 1:
    print(0)
else:
    print(dfs(0, 1, 0))
