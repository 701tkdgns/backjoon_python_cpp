import heapq

N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
hq = []
for i in lst:
    heapq.heappush(hq, i)
res = 0
for i in range(N):
    if i == 0:
        res += abs(lst[i] - lst[-1])
    else:
        res += abs(lst[i] - lst[i - 1])
print(res)