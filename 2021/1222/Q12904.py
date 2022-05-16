S, T = input(), input()
a = T
res = 0
while len(a) > len(S):
    if a[-1] == 'A':
        a = a[:-1]
    else:
        a = a[:-1]
        a = a[::-1]
    if a == S:
        res = 1
        break
print(res)
# B
# BA    ->  1
# ABB   ->  2
# ABBA  ->  1
