for _ in range(int(input())):
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    lst.sort()
    top, res = lst[0][1], 1
    for i in range(1, N):
        if lst[i][1] < top:
            top = lst[i][1]
            res += 1
    print(res)
