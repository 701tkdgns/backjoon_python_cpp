import sys
input = sys.stdin.readline
print = sys.stdout.write
N = list(map(str, input().rstrip()))
M = int(input())
R = []
# res = ''
for _ in range(M):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'L':
        if N:
            R.append(N.pop())
    elif cmd[0] == 'D':
        if R:
            N.append(R.pop())
    elif cmd[0] == 'B':
        if N: N.pop()
    elif cmd[0] == 'P':
        N.append(cmd[1])
# if R:
#     for i in N:
#         res += i
#     for i in range(len(R)-1, -1, -1):
#         res += R[i]
# else:
#     for i in N:
#         res += i
N.extend(reversed(R))
print(''.join(N))
