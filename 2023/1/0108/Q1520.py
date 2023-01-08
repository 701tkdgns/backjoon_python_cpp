import sys
sys.setrecursionlimit(10 ** 8)


def dfs(x, y):
    # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
    if x == N - 1 and y == M - 1:
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if visit[x][y] != -1:
        return visit[x][y]

    cnt = 0

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and lst[x][y] > lst[nx][ny]:
            cnt += dfs(nx, ny)

    visit[x][y] = cnt
    return visit[x][y]


N, M = map(int, input().split())
lst = []
visit = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(N):
    lst.append(list(map(int, input().split())))
print(dfs(0, 0))
