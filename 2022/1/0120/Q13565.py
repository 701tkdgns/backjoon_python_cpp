import sys
sys.setrecursionlimit(1000000)


def dfs(x, y):
    if 0 <= x < N and 0 <= y < M and lst[x][y] == 0:
        lst[x][y] = 2
        for dx, dy in direction:
            dfs(x + dx, y + dy)
        return True
    else:
        return False


N, M = map(int, sys.stdin.readline().split())  # 0 : 전류 통하는 흰색, 1 : 전류 안통하는 검은색
lst, queue = [], []
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().rstrip())))
visit = [[False for _ in range(M)] for _ in range(N)]
for i in range(M):
    dfs(0, i)
if lst[N - 1].count(2):
    print("YES")
else:
    print("NO")
