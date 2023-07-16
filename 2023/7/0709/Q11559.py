from collections import deque


def initStructure():
    return [[0 for _ in range(6)] for _ in range(12)]


def SyncData():
    tmp_dq = deque()
    tmp_chk = {"R": 0, "G": 0, "B": 0, "Y": 0, "P": 0}
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] in "RGBYP" and tmp_chk[lst[i][j]] == 0:
                tmp_dq.append([i, j, lst[i][j]])
                tmp_chk[lst[i][j]] = 1
    return tmp_dq, tmp_chk


def bfs():
    visit = initStructure()
    while True:
        dq, chk = SyncData()

        if not dq:
            break

        while dq:
            x, y, v = dq.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 12 and 0 <= ny < 6:
                    if lst[nx][ny] == v and visit[nx][ny] == 0:
                        dq.append([nx, ny, v])
                        visit[nx][ny] = 1


lst = [list(map(str, input().rstrip())) for _ in range(12)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# visit = [[0 for _ in range(6)] for _ in range(12)]
for i in lst:
    print(*i)
bfs()
