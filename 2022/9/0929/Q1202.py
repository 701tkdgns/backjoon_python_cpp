N, k = map(int, input().split())
lst = []
for _ in range(N):
    M, V = map(int, input().split())
    lst.append([M, V])
lst.sort()
K = []
for _ in range(k):
    K.append(int(input()))
K.sort()
res, idx = 0, 0
visit = [False for _ in range(k)]
while idx < k:
    s, e = 0, len(lst)-1
    _max = 0
    while s <= e:
        s += 1
    idx += 1
print(res)