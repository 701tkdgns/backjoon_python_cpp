import sys


def Cyper(n):
    if n == 0:
        ans = ' '
    elif n >= 1 and n <= 26:
        ans = chr(n + 96)
    else:
        ans = chr(n + 38)
    return ans


n = int(input())
tmp = list(map(int, sys.stdin.readline().split()))
tmpList = []
for i in tmp:
    tmpList.append(Cyper(i).lower())
tmpList.sort()
s = input()
strList = []
for i in s: strList.append(i.lower())
strList.sort()
if tmpList == strList:
    print('y')
else:
    print('n')
