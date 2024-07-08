import sys
input = sys.stdin.readline
S = list(map(str, input().rstrip()))
M = int(input())
stk = []
for _ in range(M):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'L':
        if S:
            stk.append(S.pop())
    elif cmd[0] == 'D':
        if stk:
            S.append(stk.pop())
    elif cmd[0] == 'B':
        if S:
            S.pop()
    elif cmd[0] == 'P':
        S.append(cmd[1])
S.extend(reversed(stk))
print(''.join(S))