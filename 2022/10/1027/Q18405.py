from collections import deque

def bfs():
    global dq
    new_dq = deque()
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and lst[nx][ny] == 0:
                visit[nx][ny] = visit[x][y]
                new_dq.append((nx, ny))
    dq = new_dq.copy()

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, K = map(int, input().split())
lst = []
visit = [[0 for _ in range(N)] for _ in range(N)]
dq = deque()
for x in range(N):
    tmp = list(map(int, input().split()))
    for y in range(len(tmp)):
        if tmp[y] != 0:
            dq.append([x, y])
            visit[x][y] = tmp[y]
    lst.append(tmp)
S, X, Y = map(int, input().split())
for i in range(S):
    bfs()
print(visit[X-1][Y-1])