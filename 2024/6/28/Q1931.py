import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    a, b = map(int, input().split())
    lst.append([a, b])
lst.sort(key=lambda x: (x[1], x[0]))
res, end = 0, -1
for i in range(N):
    if end <= lst[i][0]:
        end = lst[i][1]
        res += 1
print(res)
