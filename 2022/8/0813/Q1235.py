lst = []
n = int(input())
for _ in range(n):
    lst.append(input())
res = 0
L = len(lst[0])
for i in range(L - 1, -1, -1):
    tmp, tmp_idx = [], i
    chk = True
    for j in range(n):
        t = lst[j][i:]
        if t in tmp:
            chk = False
            break
        else:
            tmp.append(t)
    if chk:
        res = tmp_idx
        break
print(L-res)
