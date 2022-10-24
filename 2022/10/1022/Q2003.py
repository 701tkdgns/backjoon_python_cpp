N, M = map(int, input().split())
lst = list(map(int, input().split()))

s, e = 0, 0
res = 0
_sum = lst[s]

while s <= e < N:
    if _sum == M:
        res += 1
    if _sum <= M:
        e += 1
        if e < N:
            _sum += lst[e]
        else:
            break
        continue
    if _sum > M:
        _sum -= lst[s]
        if s == e:
            e += 1
            if e < N:
                _sum += lst[e]
            else:
                break
        s += 1
print(res)
