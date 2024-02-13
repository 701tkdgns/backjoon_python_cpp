n = int(input())
lst = list(map(int, input().split()))
cnt, mx = 0, 0
res = 0
for i in lst:
    if mx < i:
        cnt = 0
        mx = i
    else:
        cnt += 1
        res = max(res, cnt)
print(res)