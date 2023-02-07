F = input()
S = input()
T = input()

lst = [F, S, T]

for _ in range(3):
    f, s, t = F, S, T
    for i in range(len(lst)):
        f = f.replace(lst[i], "_")
        s = s.replace(lst[i], "_")
        t = t.replace(lst[i], "_")

    print(f, s, t)
    print()