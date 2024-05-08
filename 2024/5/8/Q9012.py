N = int(input())
for _ in range(N):
    stk, chk = [], True
    S = input()
    for i in S:
        if i == ")":
            if stk and stk[-1] == "(":
                stk.pop()
            else:
                chk = False
                break
        else:
            stk.append(i)
    print("NO" if not chk or stk else "YES")