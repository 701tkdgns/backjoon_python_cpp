N = int(input())
LEN = len(str(N))
F, S = 0, 0
n = str(N)
cnt = 0
for i in n:
    if cnt < LEN/2:
        F += int(i)
    else:
        S += int(i)
    cnt += 1
if F == S:
    print('LUCKY')
else:
    print('READY')