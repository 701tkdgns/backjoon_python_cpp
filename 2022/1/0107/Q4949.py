import sys
while True:
    S = sys.stdin.readline().rstrip()
    if S == '.':
        break
    stk = []
    for i in S:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(i)
                break
        elif i == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(i)
                break
    if not stk:
        print('yes')
    else:
        print('no')
