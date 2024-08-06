import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
res_idx, res_t = 0, {}
resSum, resVal = 0, 0
for i in range(1, M + 1):
    t, r = map(int, input().split())
    if resSum + r <= K:
        resSum += r
        res_t[t] = res_t.get(5, 0) + 1
    else:
        if res_idx == 0:
            res_idx = i
            resVal = min(res_t.keys())
if res_idx != 0:
    print('{} {}'.format(res_idx, resVal))
else:
    print(-1)
