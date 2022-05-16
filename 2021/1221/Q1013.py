import re

for _ in range(int(input())):
    S = input()
    P = re.compile('(100+1+|01)+')
    if P.fullmatch(S):
        print('YES')
    else:
        print('NO')