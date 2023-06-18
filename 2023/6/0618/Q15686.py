import copy
from collections import deque


def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in combination(arr[i + 1:], r - 1):
                yield [arr[i]] + nxt


def chicken_house(_lst):
    _tmp = []
    for i in range(N):
        for j in range(N):
            if _lst[i][j] == 2:
                _tmp.append([i, j])
    return _tmp


def bfs(chk, arr):
    def find_dist():
        _cnt = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 1:
                    _cnt += visit[i][j]
        return _cnt

    dq = deque(chk)
    visit = [[0 for _ in range(N)] for _ in range(N)]
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and arr[nx][ny] != 2:
                dq.append([nx, ny])
                visit[nx][ny] = visit[x][y] + 1

    cnt = find_dist()
    return cnt


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
chicken = sorted(chicken_house(lst))
res = 10000000000

for comb in combination(chicken, M):
    __lst = copy.deepcopy(lst)
    for pos in chicken:
        if pos in comb:
            continue
        else:
            __lst[pos[0]][pos[1]] = 0
    res = min(res, bfs(comb, __lst))
print(res)