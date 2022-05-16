cnt = 1
while True:
    s = input()
    stk, res = [], 0
    if s[0] == '-':
        break

    for i in s:
        if i == '}' and stk and stk[-1] == '{':
            stk.pop()
        else:
            stk.append(i)

    while stk:
        c1, c2 = stk.pop(), stk.pop()
        if c1 == c2:
            res += 1
        else:
            res += 2

    print('{}. {}'.format(cnt, res))
    cnt += 1
