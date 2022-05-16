from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    cnt = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = True
                cnt += 1
                dq.append([nx, ny])
    if cnt == 0:
        cnt = 1
    return cnt


N = int(input())
arr = []
visit = [[False for _ in range(N + 1)] for _ in range(N + 1)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
res = []
for _ in range(N):
    lst = list(map(int, input().rstrip()))
    arr.append(lst)
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visit[i][j]:
            area = bfs(i, j)
            res.append(area)
res.sort()
print(len(res))
for i in res:
    print(i)