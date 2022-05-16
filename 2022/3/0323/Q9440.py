from collections import defaultdict

while True:
    p = list(map(int, input().split()))
    numbers = defaultdict(lambda: 0)
    if p[0] == 0:
        break
    for n in p[1:]:
        numbers[n] += 1
    a, b = [], []
    chk = True
    for i in range(p[0]):
        target = None
        if chk:
            target = a
        else:
            target = b
        for j in range(10):
            if len(target) == 0 and j == 0:
                continue
            if numbers[j] > 0:
                numbers[j] -= 1
                target.append(j)
                break
        chk = not chk
    print(int("".join(map(str, a))) + int("".join(map(str, b))))