import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(v):
    visit[v] = True
    for n in lst[v]:
        if not visit[n]:
            dp[n] = dp[v] + 1
            dfs(n)

N = int(input())
lst = [[] for _ in range(N + 1)]
visit = [0 for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

dfs(1)

res = 0
for i in range(2, N + 1):
    if len(lst[i]) == 1:
        res += dp[i]

if res % 2 == 0:
    print("No")
else:
    print("Yes")