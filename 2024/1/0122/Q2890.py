R, C = map(int, input().split())
lst = []
tmp = [[] for _ in range(R)]
cnt = [C, 0]
res = [0 for _ in range(R + 1)]
for _ in range(R):
    lst.append(list(map(str, input())))
for i in range(C - 1, -1, -1):
    for j in range(R):
        if lst[j][i] not in '.FS' and tmp[int(lst[j][i])] == []:
            tmp[int(lst[j][i])] = [i, int(lst[j][i])]
tmp.sort(reverse=True)
for v in tmp:
    if v:
        if cnt[0] == v[0]:
            res[v[1]] = cnt[1]
        else:
            cnt = [v[0], cnt[1] + 1]
            res[v[1]] = cnt[1]
for i in res:
    if i == 0:
        continue
    print(i)