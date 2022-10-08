T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    res, _max = 0, 0

    for i in range(len(lst)-1, -1, -1):
        if lst[i] > _max:
            _max = lst[i]
        else:
            res += _max - lst[i]
    print(res)