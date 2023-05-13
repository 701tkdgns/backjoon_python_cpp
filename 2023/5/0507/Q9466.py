import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, res):
    visit[x] = True
    cycle.append(x)
    num = lst[x]
    if visit[num]:
        if num in cycle:
            res += cycle[cycle.index(num):]
        return
    else:
        dfs(num, res)


for _ in range(int(input())):
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    visit = [False for _ in range(n + 1)]
    res = []
    for i in range(1, n + 1):
        if not visit[i]:
            cycle = []
            dfs(i, res)
    print(n - len(res))
