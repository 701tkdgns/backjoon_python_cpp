def TM(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    if k % 2 == 1:
        return 1 - TM(k // 2)
    else:
        return TM(k // 2)


K = int(input())
res = TM(K-1)
print(res)
