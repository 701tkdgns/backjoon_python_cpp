import sys
input = sys.stdin.readline
S = list(map(str, input().rstrip()))
N = int(input())
R = []
for _ in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'L':
        if S:
            R.append(S.pop())
    elif cmd[0] == 'D':
        if R:
            S.append(R.pop())
    elif cmd[0] == 'B':
        if S:
            S.pop()
    elif cmd[0] == 'P':
        S.append(cmd[1])
S.extend(reversed(R))
print(''.join(S))