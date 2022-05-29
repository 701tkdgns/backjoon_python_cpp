for _ in range(int(input())):
    S = input()
    s = int(S)
    lst_s = sorted(list(S))
    res = 10 ** len(S)
    while s < 10 ** len(S):
        s += 1
        chk_s = sorted(list(str(s)))
        if lst_s == chk_s:
            res = min(res, s)
            break
    if res == 10**len(S):
        print('BIGGEST')
    else:
        print(res)