import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
lst = []
for _ in range(N):
    s, e = map(int, input().split())
    lst.append([s, 1])
    lst.append([e, -1])
lst.sort()
res, cnt = 0, 0
for v, point in lst:
    cnt += point
    res = max(res, cnt)
print(res)