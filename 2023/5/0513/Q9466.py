import sys

sys.setrecursionlimit(10 ** 6 + 1)
# https://www.acmicpc.net/problem/9466

def dfs(v):
    global cnt
    if finish[v]:
        return
    if visit[v]:
        finish[v] = True
        cnt += 1
    visit[v] = True
    dfs(lst[v])
    finish[v] = True
    visit[v] = False


for _ in range(int(input())):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    visit = [False for _ in range(N + 1)]
    finish = [False for _ in range(N + 1)]
    cnt = 0
    for i in range(1, N + 1):
        if not visit[i]:
            dfs(i)
    print(N - cnt)
