def dfs(v):
    global cnt
    visit[v] = True
    cnt += 1
    for i in lst[v]:
        if not visit[i]:
            dfs(i)


def bfs(v):
    global cnt
    queue = list([v])
    while queue:
        v = queue[0]
        del queue[0]
        if not visit[v]:
            visit[v] = True
            cnt += 1
            for i in lst[v]:
                if not visit[i]:
                    queue.append(i)


N = int(input())
M = int(input())
cnt = 0
lst = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()
# bfs(1)
dfs(1)
print(cnt-1)
