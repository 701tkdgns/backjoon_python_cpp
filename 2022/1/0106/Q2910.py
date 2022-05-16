N, C = map(int, input().split())
lst = list(map(int, input().split()))
dt = dict()
for i in lst:
    dt[i] = dt.get(i, 0) + 1
frequency = []
for i in dt:
    frequency.append((i, dt.get(i), lst.index(i)))
frequency.sort(key=lambda x: (-x[1], x[2]))
for k, v, i in frequency:
    for _ in range(v):
        print(k, end=' ')