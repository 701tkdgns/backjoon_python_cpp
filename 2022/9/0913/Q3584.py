import sys
sys.setrecursionlimit(10 ** 6)


for _ in range(int(input())):
    N = int(input())
    # lst = [[] for _ in range(N + 1)]
    # visit = [False for _ in range(N + 1)]
    parent = [0] * (N + 1)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a
        # lst[a].append(b)
        # lst[b].append(a)
    s, e = map(int, input().split())
    s_parent, e_parent = [0, s], [0, e]
    while parent[s]:
        s_parent.append(parent[s])
        s = parent[s]
    while parent[e]:
        e_parent.append(parent[e])
        e = parent[e]

    idx = 1
    while s_parent[-idx] == e_parent[-idx]:
        idx += 1
    print(s_parent[-idx + 1])