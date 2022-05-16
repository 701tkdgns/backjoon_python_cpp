import re
s = input()
p = re.compile('(100+1+|01)+')
if p.fullmatch(s):
    print('SUBMARINE')
else:
    print('NOISE')