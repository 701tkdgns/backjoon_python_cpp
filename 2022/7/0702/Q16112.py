import sys
std = sys.stdin

n, k = map(int, std.readline().split())
lst = list(map(int, std.readline().split()))
lst.sort()
res = 0
cnt = 0
for i in range(0, n):
    if cnt < k:
        res += lst[i] * cnt
        cnt += 1
    else:
        res += lst[i] * k
print(res)