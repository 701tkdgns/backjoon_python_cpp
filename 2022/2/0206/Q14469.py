N = int(input())
lst = []
for i in range(N):
    a, b= map(int, input().split())
    lst.append([a, b])
lst.sort(key=lambda x:x[0])
res = 0
for start, time in lst:
    if res >= start:
        res += time
    else:
        res = start + time
print(res)