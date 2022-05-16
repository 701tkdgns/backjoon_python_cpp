lst = []
for _ in range(int(input())):
    lst.append(int(input()))
lst.sort(reverse=True)
res = 0
for idx, value in enumerate(lst):
    if idx <= value:
        res += value - idx
print(res)