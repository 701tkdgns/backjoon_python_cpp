# from collections import deque
#
#
# def bfs(x, y):
#     dq = deque()
#     dq.append([x, y])
#     while dq:
#         x, y = dq.popleft()
#         visit[x][y] = True
#         for dx, dy in direction:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and lst[nx][ny] == 1:
#                 dq.append([nx, ny])
import sys

sys.setrecursionlimit(100000)


def dfs(x, y):
    visit[x][y] = True
    for dx, dy in direction:
        nx, ny = dx + x, dy + y
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and lst[nx][ny] == 1:
            dfs(nx, ny)


direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(int(input())):
    N, M, K = map(int, input().split())
    lst = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    for _ in range(K):
        a, b = map(int, input().split())
        lst[a][b] = 1

    for i in range(N):
        for j in range(M):
            if not visit[i][j] and lst[i][j] == 1:
                # bfs(i, j)
                dfs(i, j)
                cnt += 1
    print(cnt)
