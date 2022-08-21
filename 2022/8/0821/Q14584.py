S = input()
N = int(input())
lst = []
for _ in range(N):
    lst.append(input())
cnt = 1
while cnt < 27:
    tmp = ''
    chk = False
    for i in range(len(S)):
        tmp += chr((((ord(S[i]) - 97) + cnt) % 26) + 97)
    res = tmp
    for i in lst:
        tmp = tmp.replace(i, "")
        if tmp != res:
            chk = True
            break
    if chk:
        print(res)
    cnt += 1
