import sys
input = sys.stdin.readline


def dfs(x, y, s, v, direct, L, r, c):
    t = v
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and L[nx][ny] not in s:
            t = max(t, dfs(nx, ny, s + L[nx][ny], v + 1, direct, L, r, c))
    return t


R, C = map(int, input().split())
lst = []
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for _ in range(R):
    tmp = list(map(str, input().rstrip()))
    lst.append(tmp)
res = dfs(0, 0, lst[0][0], 1, direction, lst, R, C)
print(res)