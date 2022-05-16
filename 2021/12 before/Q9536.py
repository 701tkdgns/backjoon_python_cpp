N = int(input())
for _ in range(N):
    animal_sound = dict()
    txt = input().split()
    res = []
    while True:
        s = input()
        if s == 'what does the fox say?':
            break
        s = s.split()
        animal_sound[s[2]] = s[0]

    for i in txt:
        if i not in animal_sound:
            res.append(i)

    for i in res:
        print(i, end=' ')
