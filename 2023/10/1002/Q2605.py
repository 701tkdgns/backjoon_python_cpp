n = int(input())
lst = list(map(int, input().split()))
res = []
for i in range(n):
    if i == 0:
        res.append(1)
    else:
        res = res[:lst[i]] + [i + 1] + res[lst[i]:]
res.reverse()
print(*res)