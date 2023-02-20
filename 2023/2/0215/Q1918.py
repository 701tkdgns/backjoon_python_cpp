s = list(input().rstrip())
stk = []
for i in range(len(s)):
    if s[i] == '(':
        stk.append(s[i])
    if s[i] == ')':
        while stk and stk[-1] != "(":
            print(stk.pop(), end="")
        stk.pop()
    if s[i] in "*/":
        while stk and stk[-1] != "(" and stk[-1] in "*/":
            print(stk.pop(), end="")
        stk.append(s[i])
    if s[i] in "+-":
        while stk and stk[-1] != "(" :
            print(stk.pop(), end="")
        stk.append(s[i])
    if 'A' <= s[i] <= 'Z':
        print(s[i], end="")
while stk:
    print(stk.pop(), end='')

