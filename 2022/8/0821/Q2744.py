S = input()
for i in range(len(S)):
    if 65 <= ord(S[i]) <= 92:
        print(S[i].lower(), end='')
    else:
        print(S[i].upper(), end='')