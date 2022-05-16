import sys
S = []
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'add':
        if int(command[1]) in S:
            continue
        else:
            S.append(int(command[1]))
    if command[0] == 'remove':
        if int(command[1]) not in S:
            continue
        else:
            S.remove(int(command[1]))
    if command[0] == 'check':
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    if command[0] == 'toggle':
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.append(int(command[1]))
    if command[0] == 'all':
        S = [i for i in range(1, 21)]
    if command[0] == 'empty':
        S = []
