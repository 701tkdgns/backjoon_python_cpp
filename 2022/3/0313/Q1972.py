while True:
    txt = input()
    if txt == "*":
        exit()
    chk = True
    for i in range(1, len(txt)):
        lst = []
        for j in range(len(txt) - i):
            lst.append(txt[j] + txt[j + i])
        for k in range(len(lst)):
            if lst[k] in lst[k + 1:]:
                chk = False
    if chk:
        print("{} is surprising.".format(txt))
    else:
        print("{} is NOT surprising.".format(txt))
