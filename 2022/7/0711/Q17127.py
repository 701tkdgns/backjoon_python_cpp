def MUL(start, end):
    ret = lst[start]
    for i in range(start+1, end):
        ret *= lst[i]
    return ret


N = int(input())
res = 0
lst = list(map(int, input().split()))
s = 0
for i in range(N - 3):
    s = 0
    for j in range(i + 1, N - 2):
        for k in range(j + 1, N - 1):
            for r in range(k + 1, N):
                s = MUL(i, j) + MUL(j, k) + MUL(k, r) + MUL(r, N)
                res = max(res, s)
print(res)