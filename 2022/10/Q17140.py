import sys
from collections import Counter

r, c, k = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]


def R():
    copy_a = []
    max_len = 0
    for tmp in A:
        tmp = Counter(tmp)
        del (tmp[0])
        copy_tmp = sorted(tmp.items(), key=lambda x: (x[1], x[0]))
        tt = []
        for a in copy_tmp:
            tt.extend(a)
            if len(tt) == 100: break
        max_len = max(max_len, len(tt))
        copy_a.append(tt)

    for ss in copy_a:
        ss += [0] * (max_len - len(ss))
    return copy_a


time = 0
while 1:
    if time > 100:
        break
    if r <= len(A) and c <= len(A[0]) and A[r - 1][c - 1] == k:
        break
    if len(A) >= len(A[0]):
        A = R()
    else:
        A = list(map(list, zip(*A)))
        A = R()
        A = list(map(list, zip(*A)))

    time += 1
if time > 100:
    print(-1)
else:
    print(time)
