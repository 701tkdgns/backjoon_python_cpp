F = input()
S = input()
tmp = ''
chk = False
for i in F:
    if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
        tmp += i
    if tmp != '' and S in tmp:
        chk = True
        break
if chk:
    print(1)
else:
    print(0)
