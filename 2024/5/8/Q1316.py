N = int(input())
cnt = 0
for _ in range(N):
    s = input()
    chkList, chk = [], True
    for i in range(len(s)):
        if s[i] not in chkList:
            chkList.append(s[i])
        else:
            if s[i - 1] != s[i]:
                chk = False
                break
    cnt = cnt + 1 if chk else cnt
print(cnt)
