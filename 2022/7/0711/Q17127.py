def Mul(start, end):
    ret = lst[start]
    for i in range(start + 1, end + 1):
        ret *= lst[i]
    return ret


N, SUM, ANS = int(input()), 0, 0
lst = list(map(int, input().split()))
for i in range(N - 3):
    SUM = 0
    for j in range(i + 1, N - 2):
        for k in range(j + 1, N - 1):
            for r in range(k + 1, N):
                SUM = Mul(i, j - 1) + Mul(j, k - 1) + Mul(k, r - 1) + Mul(r, N)
                ANS = max(SUM, ANS)
print(ANS)
