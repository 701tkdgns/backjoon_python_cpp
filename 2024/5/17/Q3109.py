import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    if y == C - 1:
        return True
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and lst[nx][ny] == '.' and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            tmp = dfs(nx, ny)
            if tmp:
                return True
    return False


R, C = map(int, input().split())
lst = []
direction = [[-1, 1], [0, 1], [1, 1]]
visit = [[0 for _ in range(C)] for _ in range(R)]
cnt = 0
for _ in range(R):
    lst.append(list(map(str, input().rstrip())))
for j in range(R):
    if lst[j][0] == '.' and visit[j][0] == 0:
        # visit[j][0] = 1
        chk = dfs(j, 0)
        cnt = cnt + 1 if chk else cnt
print(cnt)
