def recur(_sum, sign, _num, idx, _str):
    if idx == N:
        _sum += sign * _num
        if _sum == 0:
            print(_str)
    else:
        recur(_sum, sign, _sum * 10 + (idx + 1), idx + 1, _str + ' ' + str(idx))
        recur(_sum + _num * sign, 1, idx + 1, idx + 1, _str + '+' + str(_num + 1))
        recur(_sum + _num * sign, -1, idx + 1, idx + 1, _str + '-' + str(_num + 1))


for _ in range(int(input())):
    N = int(input())
    recur(0, 1, 1, 1, '1')
