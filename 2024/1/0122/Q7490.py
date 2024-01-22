def recur(_sum, sign, n, _idx, _str):
    if _idx == N:
        _sum += n * sign
        if _sum == 0:
            print(_str)
    else:
        recur(_sum, sign, _sum * 10 + _idx + 1, _idx + 1, _str + ' ' + str(n + 1))
        recur(_sum + sign * n, 1, _idx + 1, _idx + 1, _str + '+' + str(n + 1))
        recur(_sum + sign * n, -1, _idx + 1, _idx + 1, _str + '-' + str(n + 1))


T = int(input())
for _ in range(T):
    N = int(input())
    recur(0, 1, 1, 1, '1')
