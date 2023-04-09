N = int(input())
lst = []
mx = [[0 for _ in range(N)] for _ in range(N)]
mn = [[10e9 for _ in range(N)] for _ in range(N)]
direction = [[-1, 1], [0, 1], [1, 1]]
for _ in range(N):
    lst.append(list(map(int, input().split())))
for i in range(N):
    mx[0][i] = lst[0][i]
    mn[0][i] = lst[0][i]

for i in range(N):
    if i == N - 1:
        break
    for j in range(N):
        for dx, dy in direction:
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < N:
                mx[nx][ny] = max(mx[nx][ny], lst[i][j] + lst[nx][ny])
                mn[nx][ny] = min(mn[nx][ny], lst[i][j] + lst[nx][ny])
print(mn)
print(mx)