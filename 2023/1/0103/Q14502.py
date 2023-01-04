from collections import deque
import copy


def bfs():
    global res
    dq = deque()
    tmp_lst = copy.deepcopy(lst)
    for i in range(N):
        for j in range(M):
            if tmp_lst[i][j] == 2:
                dq.append([i, j])

    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and tmp_lst[nx][ny] == 0:
                tmp_lst[nx][ny] = 2
                dq.append([nx, ny])

    tmp_res = 0
    for i in range(N):
        for j in range(M):
            if tmp_lst[i][j] == 0:
                tmp_res += 1

    res = res if res > tmp_res else tmp_res


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 0:
                lst[i][j] = 1
                makeWall(cnt + 1)
                lst[i][j] = 0


N, M = map(int, input().split())
lst = []
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(N):
    lst.append(list(map(int, input().split())))
res = 0
makeWall(0)
print(res)
