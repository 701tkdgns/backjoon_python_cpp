from collections import deque


def bfs(v):
    if visit[v]: return 0
    dq = deque([v])
    while dq:
        node = dq.popleft()
        for new_node in bfs_lst[node]:
            if not visit[new_node]:
                visit[new_node] = True
                dq.append(new_node)
                if new_node == v:
                    return 1
    return 0


T = int(input())
for _ in range(T):
    res = 0
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    bfs_lst = [[] for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]
    for idx, value in enumerate(lst):
        bfs_lst[idx].append(value)
    for i in range(1, n + 1):
        res += bfs(i)
    print(res)
