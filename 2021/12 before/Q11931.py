import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort(key=lambda x: -x)
for i in lst:
    print(i)