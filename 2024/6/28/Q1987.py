import sys

input = sys.stdin.readline


def dfs(x, y, c):
    global res
    res = max(res, c)
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not lst[nx][ny] in alpha:
            alpha.add(lst[nx][ny])
            dfs(nx, ny, c + 1)
            alpha.remove(lst[nx][ny])


R, C = map(int, input().split())
lst = [list(input()) for _ in range(R)]
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
res = 0
alpha = set()
alpha.add(lst[0][0])
dfs(0, 0, 1)
print(res)
