P = int(input())
for _ in range(P):
    lst = list(map(int, input().split()))
    T = lst[0]
    del lst[0]
    res = lst.copy()
    cnt = 0
    for i in range(len(lst)):
        mn = 10e9
        idx = 0
        for j in range(i, len(lst)):
            if mn > lst[j]:
                idx = j
                mn = lst[j]
        if i < idx:
            cnt += len(lst[i:idx])
            del lst[idx]
            lst = [mn] + lst
    print(T, cnt)