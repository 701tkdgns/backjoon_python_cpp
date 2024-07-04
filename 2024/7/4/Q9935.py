import sys
input = sys.stdin.readline
S = list(map(str, input().rstrip()))
bomb = list(map(str, input().rstrip()))
stk = []
for i in range(len(S)):
    stk.append(S[i])
    if stk[-len(bomb):] == bomb:
        cnt = len(bomb)
        while cnt > 0:
            stk.pop()
            cnt -= 1
print(''.join(stk) if stk else 'FRULA')