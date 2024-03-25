# from collections import deque
#
#
# def fbfs():
#     while fdq:
#         x, y = fdq.popleft()
#         for dx, dy in direction:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < R and 0 <= ny < C and fire[nx][ny] == 0 and lst[nx][ny] not in 'F#':
#                 fdq.append([nx, ny])
#                 fire[nx][ny] = fire[x][y] + 1
#
#
# def hbfs():
#     while hdq:
#         x, y = hdq.popleft()
#         for dx, dy in direction:
#             nx, ny = x + dx, y + dy
#             if not (0 <= nx < R and 0 <= ny < C):
#                 print(human[x][y])
#                 exit()
#             else:
#                 if lst[nx][ny] != '#' and human[x][y] + 1 < fire[nx][ny]:
#                     hdq.append([nx, ny])
#                     human[nx][ny] = human[x][y] + 1
#
#
# direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# hdq = deque([])
# fdq = deque([])
# R, C = map(int, input().split())
# lst = []
# human, fire = [[0 for _ in range(C)] for _ in range(R)], [[0 for _ in range(C)] for _ in range(R)]
# for i in range(R):
#     r = list(input().rstrip())
#     for j in r:
#         if j == 'J':
#             hdq.append([i, r.index(j)])
#             human[i][r.index(j)] = 1
#         elif j == 'F':
#             fdq.append([i, r.index(j)])
#             fire[i][r.index(j)] = 1
#     lst.append(r)
# fbfs()
# hbfs()


import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def fbfs():
    while fq:
        r, c = fq.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if maze[nr][nc] == "#" or fire[nr][nc]:
                continue
            fire[nr][nc] = fire[r][c] + 1
            fq.append((nr, nc))

def hbfs():
    while hq:
        r, c = hq.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                print(human[r][c])
                return
            if human[nr][nc] or maze[nr][nc] == "#":
                continue
            if fire[nr][nc] and human[r][c] + 1 >= fire[nr][nc]:
                continue
            human[nr][nc] = human[r][c] + 1
            hq.append((nr, nc))
    print("IMPOSSIBLE")
    return

# main
R, C = map(int, input().split())
maze = []
hq = deque()
fq = deque()
human = [[0] * C for _ in range(R)]
fire = [[0] * C for _ in range(R)]
for i in range(R):
    maze.append(list(input().strip()))
    for j in range(C):
        if maze[i][j] == "J":
            hq.append((i, j))
            human[i][j] = 1
        elif maze[i][j] == "F":
            fq.append((i, j))
            fire[i][j] = 1
fbfs()
hbfs()