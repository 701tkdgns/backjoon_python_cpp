N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
p, m = [], []
for i in range(N):
    if lst[i] > 0:
        p.append(lst[i])
    else:
        m.append(-lst[i])
p.sort(reverse=True)
m.sort(reverse=True)
tot = 0
for i in range(0, len(p), K):
    tot += (p[i] * 2)
for i in range(0, len(m), K):
    tot += (m[i] * 2)
tot -= max(abs(lst[0]), abs(lst[N - 1]))
print(tot)