N, cnt = int(input()), 0
lst = []
for _ in range(N):
    lst.append(int(input()))
stk, chk = [], []
for i in range(1, N+1):
    stk.append(i)
    chk.append('+')
    while stk and stk[-1] == lst[cnt]:
        stk.pop()
        chk.append('-')
        cnt += 1
if not stk:
    for i in chk:
        print(i)
else:
    print('NO')