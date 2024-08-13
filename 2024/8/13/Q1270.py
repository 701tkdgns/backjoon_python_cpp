import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    D = dict()
    k, v = 0, 0
    for i in range(1, len(lst)):
        D[lst[i]] = D.get(lst[i], 0) + 1
        if D[lst[i]] > lst[0] // 2 and v < D[lst[i]]:
            k = lst[i]
            v = D[lst[i]]
    print(k if k != 0 else 'SYJKGW')