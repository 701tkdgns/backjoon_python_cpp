n = int(input())
keys = []
res = []

for i in range(n):
    txt = input()
    tmp = txt.split()
    chk = False
    tmp_res = ''
    for word in tmp:
        if word[0].upper() not in keys and not chk:
            keys.append(word[0].upper())
            tmp_res += '[' + word[0] + ']' + word[1:]
            chk = True
        else:
            tmp_res += word
        tmp_res += ' '
    if not chk:
        for j, t in enumerate(txt):
            if t.upper() not in keys and t != ' ':
                tmp_res = txt[:j] + '[' + txt[j] + ']' + txt[j+1:]
                keys.append(t.upper())
                break
    res.append(tmp_res.strip())
print(*res, sep='\n')