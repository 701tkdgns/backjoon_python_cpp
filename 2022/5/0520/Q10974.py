def bt(n, depth):
    global lst, visit
    if n == depth:
        res.append(lst.copy())
        return
    for i in range(1, n + 1):
        if not visit[i]:
            visit[i] = True
            lst[depth] = i
            bt(n, depth+1)
            visit[i] = False


N = int(input())
res = []
lst = [0 for _ in range(N)]
visit = [False for _ in range(N + 1)]
bt(N, 0)
for tmp in res:
    for v in tmp:
        print(v, end=' ')
    print()