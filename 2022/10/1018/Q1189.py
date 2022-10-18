import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, y, cnt):
    global res
    if x == 0 and y == C - 1 and cnt == K:
        res += 1
        return

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not visit[nx][ny] and lst[nx][ny] != "T":
            visit[nx][ny] = True
            dfs(nx, ny, cnt + 1)
            visit[nx][ny] = False


R, C, K = map(int, input().split())
lst = []
res = 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for _ in range(R):
    lst.append(list(map(str, input().rstrip())))
visit = [[False for _ in range(C)] for _ in range(R)]
visit[R-1][0] = True
dfs(R-1, 0, 1)
print(res)
