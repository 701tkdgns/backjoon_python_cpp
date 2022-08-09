S = input()
pos1 = [0 for _ in range(26)]
pos2 = [0 for _ in range(26)]
cnt = 0
for i in range(52):
    idx = ord(S[i]) - 65
    if pos1[idx] == 0:
        pos1[idx] = i + 1
    else:
        pos2[idx] = i + 1
for i in range(26):
    for j in range(26):
        if pos1[i] < pos1[j] < pos2[i] < pos2[j]:
            cnt += 1
print(cnt)