wrong = "Impossible"
res = []
for _ in range(int(input())):
    a, b, s = map(int, input().split())

    if s == 0:
        res.append("0 0")
        continue

    if a > s and b > s:
        res.append(wrong)
        continue

    hi = a if a > b else b
    lo = a if a < b else b
    _s = s // hi

    chk = False
    v_chk = [False for _ in range(lo)]
    for i in range(_s, -1, -1):
        if chk:
            break
        else:
            rem = s - hi * i
            mod = rem % lo

            if v_chk[mod]:
                chk = False
                break

            v_chk[mod] = True
            if mod != 0: continue

            chk = True
            if hi == a:
                res.append("{} {}".format(i, (rem // lo)))
            else:
                res.append("{} {}".format((rem // lo), i))
    if not chk:
        res.append(wrong)
for i in res:
    print(i)
