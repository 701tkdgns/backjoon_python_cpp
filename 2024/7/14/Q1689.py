import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    s, e = map(int, input().split())
    lst.append([s, 1])
    lst.append([e, -1])
lst.sort()
cnt, res = 0, -1
for i, v in lst:
    cnt += v
    res = max(res, cnt)
print(res)