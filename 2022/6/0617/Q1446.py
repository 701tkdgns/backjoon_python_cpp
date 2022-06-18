N, D = map(int, input().split())
lst = [[] for _ in range(10001)]
d = [i for i in range(D + 1)]
for _ in range(N):
    start, end, speedway = map(int, input().split())
    lst[start].append([speedway, end])
for i in range(D + 1):
    if i != 0:
        d[i] = min(d[i], d[i - 1] + 1)
    for speedway, end in lst[i]:
        if end <= D and speedway + d[i] < d[end]:
            d[end] = speedway + d[i]
print(d[D])