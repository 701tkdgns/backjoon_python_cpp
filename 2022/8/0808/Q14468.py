S = input()
pos1 = []
pos2 = []
cnt = 0
for i in range(52):
    idx = ord(S[i]) - 65
    if pos1[idx] == 0:
        pos1[idx] = i + 1
    else:
        pos2[idx] = i + 1
for i in range(26):
    for j in range(26):
        if pos1[i] < pos2[j] and pos1[j] < pos2[i] < pos2[j]:
            cnt += 1
print(cnt)