import sys
std = sys.stdin.readline

N = int(std())
lst = list(map(int, std().split()))
cnt = 0
lst.sort()
for i in range(N):
    tmp = lst[:i] + lst[i+1:]
    s, e = 0, len(tmp) - 1
    while s < e:
        t = tmp[s] + tmp[e]
        if t == lst[i]:
            cnt += 1
            break
        if t < lst[i]:
            s += 1
        else:
            e -= 1
print(cnt)
