while True:
    try:
        s, t = input().split()
        idx = 0
        chk = False
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
            if idx == len(s):
                chk = True
                break
        if chk:
            print('Yes')
        else:
            print('No')
    except:
        break
