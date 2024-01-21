def recur(_sum, sign, _num, idx, _str):
    if idx == N:
        _sum += sign * _num
        if _sum == 0:
            print(_str)
    else:
        recur(_sum, sign, _num * 10 + (idx + 1), idx + 1, _str + ' ' + str(idx + 1))
        recur(_sum + sign * _num, 1, idx + 1, idx + 1, _str + '+' + str(idx + 1))
        recur(_sum + sign * _num, -1, idx + 1, idx + 1, _str + '-' + str(idx + 1))


T = int(input())
for _ in range(T):
    N = int(input())
    recur(0, 1, 1, 1, '1')

#https://velog.io/@tks7205/%EB%B0%B1%EC%A4%80-7490-0%EB%A7%8C%EB%93%A4%EA%B8%B0backtracking