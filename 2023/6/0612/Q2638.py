import copy
from collections import deque


def delCheese():
    global dq
    q = copy.deepcopy(dq)
    dq = deque()
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and ((not visit[nx][ny] and not lst[nx][ny]) or lst[nx][ny] == 1):
                visit[nx][ny] += 1
                if lst[nx][ny] == 1 and visit[nx][ny] >= 2:
                    dq.append([nx, ny])
                if lst[nx][ny] == 0:
                    q.append([nx, ny])
    for x, y in dq:
        lst[x][y] = 0


N, M = map(int, input().split())
lst = []
visit = [[0 for _ in range(M)] for _ in range(N)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dq = deque()
for _ in range(N):
    lst.append(list(map(int, input().split())))
dq = deque()
dq.append([0, 0])

cnt = 0
while dq:
    delCheese()
    if dq:
        cnt += 1

print(cnt)
