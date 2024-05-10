# N = int(input())
K = list(map(int, input().rstrip()))

res = 0
for i in range(len(K)):
    if i == len(K) - 1:
        res += 1
        break
    if res >= K[i]:
        res += 10
    else:
        res = K[i]
print(res)