import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = []

_max = sys.maxsize

for i in range(N - 2):
    s, e = i + 1, N - 1
    while s < e:
        tmp = lst[s] + lst[i] + lst[e]
        if abs(tmp) <= _max:
            _max = abs(tmp)
            res = [lst[i], lst[s], lst[e]]
        if tmp > 0:
            e -= 1
        elif tmp < 0:
            s += 1
        else:
            break
print(*res)
