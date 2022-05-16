from collections import deque

def init(n):
    return [False for _ in range(n+1)]

def dfs(v):
    print(v, end=' ')
    check[v] = True
    for i in lst[v]:
        if not check[i]:
            dfs(i)

def bfs(v):
    dq = deque([v])
    while dq:
        v = dq.popleft()
        if not check[v]:
            print(v, end=' ')
            check[v] = True
            for i in lst[v]:
                if not check[i]:
                    dq.append(i)

N, M, V = map(int, input().split())
lst = [[] for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for i in lst:
    i.sort()

check = init(N)
dfs(V)
print()
check = init(N)
bfs(V)
