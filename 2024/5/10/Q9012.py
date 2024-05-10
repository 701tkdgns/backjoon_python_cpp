for _ in range(int(input())):
    s = input()
    stk, chk = [], False
    for i in s:
        if i == ")":
            if stk and stk[-1] == "(":
                stk.pop()
            else:
                chk = True
                break
        else:
            stk.append(i)
    print('NO' if stk or chk else 'YES')
