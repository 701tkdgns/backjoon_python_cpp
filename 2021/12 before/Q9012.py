N = int(input())
for _ in range(N):
    S = input()
    stk = []
    for i in S:
        if i == '(':
            stk.append(i)
        else:
            if stk:
                stk.pop()
            else:
                stk.append(i)
                break
    if stk:
        print('NO')
    else:
        print('YES')