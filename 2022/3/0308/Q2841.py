N, P = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
cnt = 0
stk = [[] for _ in range(7)]
for idx, p in arr:
    if len(stk[idx]) == 0:
        stk[idx].append(p)
        cnt += 1
    else:
        if p > stk[idx][-1]:
            stk[idx].append(p)
            cnt += 1
        elif p == stk[idx][-1]:
            continue
        else:
            while stk[idx] and stk[idx][-1] > p:
                stk[idx].pop()
                cnt += 1
            if stk[idx] and stk[idx][-1] == p:
                continue
            stk[idx].append(p)
            cnt += 1
print(cnt)
