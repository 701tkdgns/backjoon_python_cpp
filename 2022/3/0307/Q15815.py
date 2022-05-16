S = input()
stk = []
for i in S:
    if i == '+':
        a, b = stk.pop(), stk.pop()
        stk.append((b + a))
    elif i == '-':
        a, b = stk.pop(), stk.pop()
        stk.append((b - a))
    elif i == '*':
        a, b = stk.pop(), stk.pop()
        stk.append((b * a))
    elif i == '/':
        a, b = stk.pop(), stk.pop()
        stk.append((b // a))
    else:
        stk.append(int(i))
print(stk.pop())
