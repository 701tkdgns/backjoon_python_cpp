poem = list(input().split())
space = int(input())
alphabet = list(map(int, input().split()))

if len(poem) - 1 > space:
    print(-1)
else:
    answer = True
    title = ''
    idx = 0
    while answer and idx < len(poem):
        s = poem[idx]
        i = 0
        while i < len(s):
            if i >= 1 and s[i] == s[i-1]:
                i += 1
                continue
            if alphabet[ord(s[i].upper())-65]:
                alphabet[ord(s[i].upper())-65] -= 1
            else:
                answer = False
                break
            i += 1
        idx += 1
        if answer:
            title = s[0].upper()
    if answer:
        tmp = title.lower()
        i = 0
        while i < len(tmp):
            if i >= 1 and tmp[i] == tmp[i-1]:
                i += 1
                continue
            if alphabet[ord(tmp[i])-97]:
                alphabet[ord(tmp[i])-97] -= 1
            else:
                answer = False
                break
            i += 1
        if answer:
            print(title)
        else:
            print(-1)
    else:
        print(-1)