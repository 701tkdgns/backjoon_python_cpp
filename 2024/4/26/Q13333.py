N = int(input())
lst = list(map(int, input().split()))
lst.sort()
q = 0
for k in range(N, -1, -1):
    if k <= lst[-k]:
        q = k
        break
print(q)