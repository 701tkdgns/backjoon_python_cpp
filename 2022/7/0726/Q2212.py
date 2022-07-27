N = int(input())
K = int(input())
lst = sorted(list(map(int, input().split())))

if K >= N:
    print(0)
    exit()

dist = []
for i in range(1, N):
    dist.append(lst[i]- lst[i-1])

dist.sort(reverse=True)
for _ in range(K - 1):
    dist.pop(0)

print(sum(dist))