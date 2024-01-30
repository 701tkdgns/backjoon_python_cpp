def dfs(i, j, _sum, cnt):
    global res
    if cnt == 4:
        res = max(res, _sum)
        return
    for n in range(4):
        ni, nj = i + mv[n][0], j + mv[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visit[ni][nj]:
            visit[ni][nj] = True
            dfs(ni, nj, _sum + lst[ni][nj], cnt + 1)
            visit[ni][nj] = False


def exec(i, j):
    global res
    for n in range(4):
        tmp = lst[i][j]
        for k in range(3):
            t = (n + k) % 4
            ni, nj = i + mv[t][0], j + mv[t][1]
            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += lst[ni][nj]
        res = max(res, tmp)


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
mv = [[0, 1], [1, 0], [0, -1], [-1, 0]]
visit = [[False for _ in range(M)] for _ in range(N)]
res = -1

for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visit[i][j] = True
        dfs(i, j, lst[i][j], 1)
        visit[i][j] = False

        exec(i, j)

print(res)