N = int(input())
lst = []
res = 0
for _ in range(N):
    a, b = (map(int, input().split()))
    lst.append([a, 1])
    lst.append([b, -1])
lst.sort()
tot, cnt = 0, 0
for line, point in lst:
    cnt += point
    tot = max(tot, cnt)
print(tot)