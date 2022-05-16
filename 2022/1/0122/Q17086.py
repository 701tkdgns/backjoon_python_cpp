# from collections import deque
#
#
# def bfs():
#     while dq:
#         x, y = dq.popleft()
#         for dx, dy in direction:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 0:
#                 dq.append([nx, ny])
#                 lst[nx][ny] = lst[x][y] + 1
#     return
#
#
# N, M = map(int, input().split())
# direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
# lst = []
# mx = 0
# dq = deque()
# for i in range(N):
#     lst.append(list(map(int, input().split())))
# for i in range(N):
#     for j in range(M):
#         if lst[i][j] == 1:
#             dq.append((i, j))
# bfs()
# for i in lst:
#     for j in i:
#         mx = max(j, mx)
# print(mx - 1)


from collections import deque


def bfs():
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 0:
                dq.append([nx, ny])
                lst[nx][ny] = lst[x][y] + 1
    return


N, M = map(int, input().split())
lst = []
direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
for i in range(N):
    lst.append(list(map(int, input().split())))
mx = 0
dq = deque()
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            dq.append([i, j])
bfs()
for i in lst:
    for j in i:
        mx = max(mx, j)
print(mx-1)