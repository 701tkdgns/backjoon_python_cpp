S = input()
stk = []
d = {"H": 1, "C": 12, "O": 16}
for i in S:
    if i == "(":
        stk.append(i)
    elif i in d:
        stk.append(d[i])
    elif i == ")":
        tmp = 0
        while True:
            p = stk.pop()
            if p == "(":
                break
            tmp += p
        if tmp != 0:
            stk.append(tmp)
    else:
        n = stk.pop()
        tmp = n * int(i)
        stk.append(tmp)
print(sum(stk))