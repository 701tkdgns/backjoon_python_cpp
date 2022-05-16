s = input()
lst = ['pi', 'ka', 'chu']
for i in lst:
    s = s.replace(i, ' ')
chk = True
for char in s:
    if ord('a') <= ord(char) <= ord('z'):
        print("NO")
        chk = False
        break
if chk:
    print("YES")
