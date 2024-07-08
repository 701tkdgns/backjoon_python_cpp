import sys


def dfs(x, y, s):
    global res
    res = max(res, len(s))
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and lst[nx][ny] not in s:
            dfs(nx, ny, s + lst[nx][ny])


input = sys.stdin.readline
R, C = map(int, input().split())
lst = []
direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]
res = 0
for _ in range(R):
    tmp = list(map(str, input().rstrip()))
    lst.append(tmp)
dfs(0, 0, lst[0][0])
print(res)