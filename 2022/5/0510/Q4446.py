a = ['a', 'i', 'y', 'e', 'o', 'u']
b = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
while True:
    try:
        S = input()
        ans = ''
        for i in range(len(S)):
            if 65 <= ord(S[i]) <= 90:
                tmp = S[i].lower()
                if tmp in a:
                    idx = (a.index(tmp) + 3) % len(a)
                    ans += a[idx].upper()
                else:
                    idx = (b.index(tmp) + 10) % len(b)
                    ans += b[idx].upper()
            elif 97 <= ord(S[i]) <= 122:
                if S[i] in a:
                    idx = (a.index(S[i]) + 3) % len(a)
                    ans += a[idx]
                else:
                    idx = (b.index(S[i]) + 10) % len(b)
                    ans += b[idx]
            else:
                ans += S[i]
        print(ans)
    except:
        break
