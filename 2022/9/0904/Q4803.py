from collections import deque


def find_tree(v):
    flag = True
    dq = deque()
    dq.append(v)
    while dq:
        now = dq.popleft()
        if visit[now]:
            flag = False
        visit[now] = True
        for next in lst[now]:
            if not visit[next]:
                dq.append(next)
    return flag


cnt = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    lst = [[] for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]
    res = 0
    for _ in range(m):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    for i in range(1, n + 1):
        if visit[i]:
            continue
        if find_tree(i):
            res += 1
    if res == 0:
        print("Case {}: No trees.".format(cnt))
    elif res == 1:
        print("Case {}: There is one tree.".format(cnt))
    else:
        print("Case {}: A forest of {} trees.".format(cnt, res))
    cnt += 1
