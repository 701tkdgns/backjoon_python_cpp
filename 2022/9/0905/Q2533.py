import sys

sys.setrecursionlimit(10 ** 9)
std = sys.stdin.readline

N = int(std())
c = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]  # dp [내자식 노드 count][내가 얼리어답터인 경우 최적해], dp [내자식 노드 count][내가 얼리어답터가 아닌 경우 최적해],
for _ in range(N - 1):
    a, b = map(int, std().split())
    c[a].append(b)
    c[b].append(a)
visit = [0 for _ in range(N + 1)]


def dfs(start):
    visit[start] = 1
    if len(c[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0
    else:
        for i in c[start]:
            if visit[i] == 0:
                dfs(i)
                dp[start][1] += min(dp[i][0], dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1


dfs(1)
print(dp)

#https://ddggblog.tistory.com/211