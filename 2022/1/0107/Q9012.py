for _ in range(int(input())):
    S = input()
    stk, chk = [], True
    for i in S:
        if i == ')':
            if stk:
                if stk[-1] == '(':
                    stk.pop()
            else:
                chk = False
                break
        else:
            stk.append(i)
    if stk or not chk:
        print('NO')
    else:
        print('YES')
