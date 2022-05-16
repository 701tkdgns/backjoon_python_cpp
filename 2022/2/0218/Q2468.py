from collections import deque


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] >= k and not visit[nx][ny]:
                dq.append([nx, ny])
                visit[nx][ny] = True


N = int(input())
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
lst, tmp_max = [], 0
res = 1
for _ in range(N):
    tmp = list(map(int, input().split()))
    tmp_max = max(tmp)
    lst.append(tmp)
for k in range(2, tmp_max + 1):
    visit = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and lst[i][j] >= k:
                cnt += 1
                visit[i][j] = True
                bfs(i, j)
    res = max(res, cnt)
print(res)
