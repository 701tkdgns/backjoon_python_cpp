res = []
for _ in range(int(input())):
    lst = []
    chk = True
    for _ in range(int(input())):
        lst.append(input())
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                S = lst[i] + lst[j]
                reverse_S = S[::-1]
                if S == reverse_S:
                    res.append(S)
                    chk = False
            if not chk:
                break
        if not chk:
            break
    if chk:
        res.append(0)
for i in res:
    print(i)