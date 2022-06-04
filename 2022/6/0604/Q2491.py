def long(n):
    cnt = 1
    mx = 0
    tmp = lst[0]
    for i in range(1, n):
        if tmp <= lst[i]:
            cnt += 1
        else:
            mx = max(mx, cnt)
            cnt = 1
        tmp = lst[i]
    mx = max(mx, cnt)
    return mx


def short(n):
    cnt = 1
    mx = 0
    tmp = lst[0]
    for i in range(1, n):
        if tmp >= lst[i]:
            cnt += 1
        else:
            mx = max(mx, cnt)
            cnt = 1
        tmp = lst[i]
    mx = max(mx, cnt)
    return mx


if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    if len(lst) == 1:
        print(1)
    else:
        res = max(long(N), short(N))
        print(res)