S = input()  # 00110000 > 0010이 나와야함
cnt_0, cnt_1 = S.count('0')//2, S.count('1')//2
chk = [True for _ in range(len(S))]
res = ""
for i in range(len(S)):
    if cnt_1 > 0 and S[i] == '1':
        cnt_1 -= 1
        chk[i] = False
for i in range(len(S)-1, -1, -1):
    if cnt_0 > 0 and S[i] == '0':
        cnt_0 -= 1
        chk[i] = False
for i in enumerate(chk):
    if i[1]:
        res += S[i[0]]
print(res)