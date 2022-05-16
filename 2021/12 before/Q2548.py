import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
res, m = max(lst), sum(lst)
for i in lst:
    SUM = 0
    for j in lst:
        SUM += abs(i-j)
    if SUM <= m and res > i:
        m = SUM
        res = i

print(res)