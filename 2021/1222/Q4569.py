t, f = 'is acceptable.', 'is not acceptable.'
while True:
    W = input()
    if W == 'end':
        break
    F, S, T = 1, 1, 1
    f_cnt = 0
    v, c = 0, 0

    for i in range(len(W)):
        if W[i] not in 'aeiou':
            f_cnt += 1
            c += 1
            v = 0
            if i - 1 >= 0 and W[i] == W[i - 1]:
                S = 0
        else:
            v += 1
            c = 0
            if i - 1 >= 0 and W[i] == W[i - 1]:
                if not (W[i] == 'e' or W[i] == 'o'):
                    S = 0
        if v >= 3 or c >= 3:
            T = 0

    if len(W) == f_cnt:
        F = 0

    if F * S * T == 1:
        print('<{}> {}'.format(W, t))
    else:
        print('<{}> {}'.format(W, f))
