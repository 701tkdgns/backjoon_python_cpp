import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    lst = []
    for _ in range(N):
        a, b = map(int, input().split())
        lst.append([a, b])
    lst.sort(key=lambda x: (x[0], x[1]))
    ent, res = lst[0][1], 1
    for i in range(1, N):
        if lst[i][1] < ent:
            ent = lst[i][1]
            res += 1
    print(res)