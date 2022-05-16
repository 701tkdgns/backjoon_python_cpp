ans = []
for _ in range(int(input())):
    S = input()
    tmp = ''
    for i in S:
        if 97 <= ord(i) <= 122:
            if tmp:
                ans.append(int(tmp))
                tmp = ''
            else:
                tmp = ''
        else:
            tmp += i
    if tmp:
        ans.append(int(tmp))
ans.sort()
for i in ans:
    print(i)