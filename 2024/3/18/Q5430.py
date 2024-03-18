import re, sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    p = input()
    n = int(input())
    arr = deque([list(map(int, re.sub(r'[\[\],]', ' ', input()).split()))])
    res = ''
    for i in p:
        if i == 'R':
            arr.reverse()
        else:
            if arr:
                arr.popleft()
            else:
                res = 'error'
                break

    if res == '':
        res = arr
    print(res)