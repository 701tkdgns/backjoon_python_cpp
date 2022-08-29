from collections import deque


def bfs(r, c):
    dq = deque()
    dq.append([r, c])
    visit[r][c] = 0
    while dq:
        r, c = dq.popleft()
        if r == r2 and c == c2:
            return
        direction = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
        for dr, dc in direction:
            nr, nc = dr + r, dc + c
            if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == -1:
                visit[nr][nc] = visit[r][c] + 1
                dq.append([nr, nc])


N = int(input())
visit = [[-1 for _ in range(N)] for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
bfs(r1, c1)
print(visit[r2][c2])