N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    lst = list(map(int, input().split()))
    tar = 0
    res = 1
    for i in range(N - 1, -1, -1):
        tar += lst[i]
        if tar > M:
            res += 1
            tar = lst[i]
    print(res)