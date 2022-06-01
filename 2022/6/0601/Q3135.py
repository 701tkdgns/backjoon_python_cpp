start, end = map(int, input().split())
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
for i in range(N):
    lst[i] = abs(end-lst[i])
print(min(min(lst)+1, abs(end-start)))
