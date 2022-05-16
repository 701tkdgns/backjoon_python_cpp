import sys
sys.setrecursionlimit(100000)

def init():
    return [False for _ in range(N+1)]

def dfs(v):
    visit[v] = True
    print(v, end=' ')
    for i in lst[v]:
        if not visit[i]:
            dfs(i)

def bfs(v):
    queue = list([v])
    while queue:
        v = queue[0]
        del queue[0]
        if not visit[v]:
            print(v, end=' ')
            visit[v] = True
            for i in lst[v]:
                if not visit[i]:
                    queue.append(i)


N, M, V = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()
visit = init()
dfs(V)
print()
visit = init()
bfs(V)