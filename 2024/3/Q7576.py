from collections import deque

M, N = map(int, input().split())
lst = []
visit = [[-1 for _ in range(M)] for _ in range(N)]
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dq = deque([])
cnt = -1
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            dq.append([i, j])
            visit[i][j] = 0
        elif tmp[j] == -1:
            visit[i][j] = -2
    lst.append(tmp)

while dq:
    x, y = dq.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if visit[nx][ny] == -1 and lst[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                dq.append([nx, ny])

for i in range(N):
    chk = True
    for j in range(M):
        if visit[i][j] == -2:
            continue
        elif visit[i][j] == -1:
            chk = False
            break
        else:
            cnt = max(cnt, visit[i][j])
    if not chk:
        cnt = -1
        break
print(cnt)
