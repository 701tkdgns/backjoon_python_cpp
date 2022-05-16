for _ in range(int(input())):
    m = input()
    msg, res = [0 for _ in range(26)], 'OK'
    chk = False
    for i in range(len(m)):
        if chk:
            chk = False
            continue
        msg[ord(m[i])-65] += 1
        if msg[ord(m[i])-65] == 3:
            if i == len(m) - 1:
                res = 'FAKE'
                break
            elif m[i] != m[i+1]:
                res = 'FAKE'
                break
            chk = True
            msg[ord(m[i])-65] = 0
    print(res)
