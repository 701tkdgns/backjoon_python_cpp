N = int(input())
lst = list(map(int, input().split()))
benefit, res = 0, 0
for i in range(N - 1, -1, -1):
    benefit = max(benefit, lst[i])
    res = max(res, benefit - lst[i])
print(res)