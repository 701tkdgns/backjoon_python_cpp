# import sys
# from collections import deque
#
#
# input = sys.stdin.readline
#
# def biteFish(init_x, init_y, shark_size):
#     dist = [[0] * N for _ in range(N)]
#     visit = [[0] * N for _ in range(N)]
#     dq = deque()
#     dq.append([init_x, init_y])
#     visit[init_x][init_y] = 1
#     chk = []
#     while dq:
#         x, y = dq.popleft()
#         for dx, dy in direction:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
#                 if lst[nx][ny] <= shark_size:
#                     dq.append([nx, ny])
#                     visit[nx][ny] = 1
#                     dist[nx][ny] = dist[x][y] + 1
#                     if lst[nx][ny] < shark_size and lst[nx][ny] != 0:
#                         chk.append([nx, ny, dist[nx][ny]])
#     return sorted(chk, key=lambda x: (-x[2], -x[0], -x[1]))
#
#
# N = int(input())
# lst = []
# direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# cnt, res = 0, 0
# x, y, size = 0, 0, 2
# for i in range(N):
#     t = list(map(int, input().split()))
#     for j in range(N):
#         if t[j] == 9:
#             x, y = i, j
#     lst.append(t)
#
# while True:
#     shark = biteFish(x, y, size)
#     if len(shark) == 0:
#         break
#
#     nx, ny, dist = shark.pop()
#     res += dist
#     lst[x][y], lst[nx][ny] = 0, 0
#     x, y = nx, ny
#     cnt += 1
#     if cnt == size:
#         size += 1
#         cnt = 0
#
# print(res)

from collections import deque


def bfs(init_x, init_y, shark_size):
    dist = [[0 for _ in range(N)] for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    chk = []
    dq = deque([[init_x, init_y]])
    visit[init_x][init_y] = 1
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                if lst[nx][ny] <= shark_size:
                    dq.append([nx, ny])
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    if lst[nx][ny] < shark_size and lst[nx][ny] != 0:
                        chk.append([nx, ny, dist[nx][ny]])
    return sorted(chk, key=lambda x: (-x[2], -x[0], -x[1]))


N = int(input())
lst = []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
x, y, size = 0, 0, 2
cnt, res = 0, 0

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 9:
            x, y = i, j
    lst.append(tmp)

while True:
    shark = bfs(x, y, size)
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop()
    res += dist
    lst[x][y], lst[nx][ny] = 0, 0
    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(res)
