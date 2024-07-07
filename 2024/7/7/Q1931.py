import sys
input = sys.stdin.readline
N = int(input())
lst = []
cnt, end = 0, 0
for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])
lst.sort(key=lambda x:(x[1], x[0]))
for s, e in lst:
    if end <= s:
        cnt += 1
        end = e
print(cnt)