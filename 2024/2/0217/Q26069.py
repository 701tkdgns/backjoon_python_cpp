N = int(input())
d = set()
d.add('ChongChong')
for _ in range(N):
    a, b = input().split()
    if a in d:
        d.add(b)
    if b in d:
        d.add(a)
print(len(d))
