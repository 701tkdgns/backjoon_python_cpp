S = input()
stk = []
length = 0
tmp = ''
for c in S:
    if c.isdigit():
        length += 1
        tmp = c
    elif c == '(':
        stk.append((tmp, length-1))
    else:
        multi, preL = stk.pop()
        length = (int(multi) * length) + preL
print(length)
