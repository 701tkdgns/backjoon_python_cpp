N, M = map(int, input().split())
lst = []
direction = [[1, 0], [0, 1], [1, 1]]
dp = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    lst.append(list(map(int, input().split())))
dp[0][0] = lst[0][0]

for x in range(N):
    for y in range(M):
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                dp[nx][ny] = max(dp[nx][ny], dp[x][y] + lst[nx][ny])

print(dp[N-1][M-1])