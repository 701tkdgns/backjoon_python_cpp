T = int(input())
for i in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    res = []
    while lst:
        t = lst[0]
        del lst[0]
        for idx, v in enumerate(lst):
            if t == int(v * 0.75):
                res.append(t)
                del lst[idx]
                break
    print("Case #{}:".format(i), end=' ')
    for v in res:
        print(v, end=' ')
