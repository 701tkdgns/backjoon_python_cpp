N = list(input())
M = int(input())
stk = []
for _ in range(M):
    command = list(input().split())
    if command[0] == "L":
        if N:
            stk.append(N.pop())
    elif command[0] == "D":
        if N:
            N.append(stk.pop())
    elif command[0] == "B":
        if N:
            N.pop()
    else:
        N.append(command[1])
N.extend(reversed(stk))
print(''.join(N))