n, w = map(int, input().split())
s = []
cnt, r = 0, 0
res = 0
for i in range(n):
    s.append(int(input()))
for i in range(len(s) - 1):
    if i == 0:
        cnt = w // s[i]
        r = w % s[i]
    elif s[i-1] < s[i] and s[i] > s[i+1]:
        res += s[i] * cnt + r
        cnt, r = 0, 0
    elif s[i-1] > s[i] and s[i] < s[i+1]:
        cnt = res // s[i]
        r = res % s[i]

res = cnt * (len(s) - 1) + r
print(res)