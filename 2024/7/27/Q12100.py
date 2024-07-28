from collections import deque


def getGraph():
    N = int(input())
    graph = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        graph.append(tmp)
    return graph, N


def up(tmp):
    for i in range(n):
        dq = deque([])
        for j in range(n):
            if tmp[n * j + i] == 0: continue
            dq.append(tmp[n * j + i])
        dq_tmp = deque([])
        while dq:
            dq_tmp.append(dq.popleft())
            if dq and dq[0] == dq_tmp[-1]:
                dq_tmp[-1] *= 2
                dq.popleft()
        dq_tmp += [0] * (n - len(dq_tmp))
        for j in range(n):
            tmp[n * j + i] = dq_tmp[j]
    return tmp


def down(temp):
    for i in range(n):
        q = deque([])
        for j in range(n):
            if temp[-n * (j + 1) + i] == 0: continue
            q.append(temp[-n * (j + 1) + i])
        ttemp = deque([])
        while q:
            ttemp.append(q.popleft())
            if q and q[0] == ttemp[-1]:
                ttemp[-1] *= 2
                q.popleft()
        ttemp += [0] * (n - len(ttemp))
        for j in range(n):
            temp[-n * (j + 1) + i] = ttemp[j]
    return temp


def left(temp):
    for i in range(n):
        q = deque([])
        for j in range(n):
            if temp[n * i + j] == 0: continue
            q.append(temp[n * i + j])
        ttemp = deque([])
        while q:
            ttemp.append(q.popleft())
            if q and q[0] == ttemp[-1]:
                ttemp[-1] *= 2
                q.popleft()
        ttemp += [0] * (n - len(ttemp))
        for j in range(n):
            temp[n * i + j] = ttemp[j]
    return temp


def right(temp):
    for i in range(n):
        q = deque([])
        for j in range(n):
            if temp[n * (i + 1) - j - 1] == 0: continue
            q.append(temp[n * (i + 1) - j - 1])
        ttemp = deque([])
        while q:
            ttemp.append(q.popleft())
            if q and q[0] == ttemp[-1]:
                ttemp[-1] *= 2
                q.popleft()
        ttemp += [0] * (n - len(ttemp))
        for j in range(n):
            temp[n * (i + 1) - j - 1] = ttemp[j]
    return temp


def dfs(level, tmp):
    global res
    if max(tmp) <= res // (2 ** (5 - level + 1)): return
    if level == 5:
        res = max(res, max(tmp))
        return
    dfs(level + 1, up(tmp[""]))
    dfs(level + 1, down(tmp[""]))
    dfs(level + 1, left(tmp[""]))
    dfs(level + 1, right(tmp[""]))


def main():
    global n, res
    graph, n = getGraph()
    res = 0
    dfs(0, graph)
    print(res)


if __name__ == "__main__":
    main()
