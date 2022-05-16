N, L = map(int, input().split())
lst = sorted(list(map(int, input().split())))
chk = [False for _ in range(1001)]
res = 0
for i in lst:
    if not chk[i]:
        for j in range(i, min(i+L, 1001)):
            chk[j] = True
        res += 1
print(res)