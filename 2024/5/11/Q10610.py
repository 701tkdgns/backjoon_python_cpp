N = input()
lst = []
v = 0
for i in range(len(N)):
    v += ord(N[i]) - ord('0')
    lst.append(ord(N[i]) - ord('0'))
lst.sort()
if lst[0] == 0 and v % 3 == 0:
    for i in range(len(N)-1, -1, -1):
        print(lst[i], end='')
else:
    print(-1)