N, K = map(int, input().split())
lst = list(map(int, input().split()))
cost = []
for i in range(N - 1):
    cost.append(lst[i+1]-lst[i])
cost.sort()
print(sum(cost[:N-K]))