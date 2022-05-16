n = int(input())
lst = [[] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    lst[i] = [a, b]
lst.sort(key=lambda x: (x[1], x[0]))
res = 0
for i in range(n):
    s = 2 * 10**9 + 1
    if 0 <= i < n - 1 and lst[i][1] == lst[i + 1][1]:
        s = min(s, abs(lst[i][0] - lst[i + 1][0]))
    if 0 < i < n and lst[i][1] == lst[i - 1][1]:
        s = min(s, abs(lst[i][0] - lst[i - 1][0]))
    if s == 2 * 10**9 + 1:
        s = 0
    res += s
print(res)
