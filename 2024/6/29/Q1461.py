N, M = map(int, input().split())
lst = list(map(int, input().split()))
p, m = [], []
lst.sort()
for i in lst:
    if i > 0:
        p.append(i)
    else:
        m.append(abs(i))
p.sort(reverse=True)
m.sort(reverse=True)
res = 0
for i in range(0, len(p), M):
    res += (p[i]*2)
for i in range(0, len(m), M):
    res += (m[i]*2)
res -= max(abs(lst[0]), abs(lst[N - 1]))
print(res)