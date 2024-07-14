import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
p, m = [], []
for v in lst:
    if v > 0:
        p.append(v)
    else:
        m.append(v)
p.sort(reverse=True)
m.sort()
res = 0
for i in range(0, len(p), M):
    res += (abs(p[i]) * 2)
for i in range(0, len(m), M):
    res += (abs(m[i]) * 2)
if not p:
    res -= abs(m[0])
elif not m:
    res -= p[0]
else:
    tmp = max(p[0], abs(m[0]))
    res -= tmp
print(res)