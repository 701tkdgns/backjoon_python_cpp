N = int(input())
line = []
for _ in range(N):
    line.append(int(input()))
key_set = set(line)
res = 1
for i in key_set:
    tmp = []
    for v in line:
        if i != v:
            tmp.append(v)
    cnt = 0
    tmp_v = tmp[0]
    for idx in range(len(tmp)):
        if tmp[idx] == tmp_v:
            cnt += 1
        else:
            res = max(cnt, res)
            cnt = 1
            tmp_v = tmp[idx]
    res = max(cnt, res)
print(res)
