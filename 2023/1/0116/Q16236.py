from collections import deque


def bfs(init_x, init_y, s):
    dq = deque()
    dq.append([init_x, init_y])
    cand = []
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                pass
    return cand

N = int(input())
lst = []
visit = [[False for _ in range(N)] for _ in range(N)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
start_x, start_y = 0, 0
shark = 2
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 9:
            start_x, start_y = i, j
            tmp[j] = 0
    lst.append(tmp)

bfs(start_x, start_y, shark)
