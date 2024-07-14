N = int(input())
lst = []
cnt, mx = 0, 0
for _ in range(N):
    s, e = map(int, input().split())
    lst.append([s, e])
lst.sort(key=lambda x: (x[1], x[0]))
for s, e in lst:
    if mx <= s:
        cnt += 1
        mx = e
print(cnt)
