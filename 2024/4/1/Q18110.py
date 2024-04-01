def _round(_v):
    if _v - int(_v) >= 0.5:
        return int(_v) + 1
    else:
        return int(_v)


N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
v = _round(N * 0.15)
lst.sort()
if N == 0:
    print(0)
else:
    print(_round(sum(lst[v:N-v]) / (N - (2 * v))))