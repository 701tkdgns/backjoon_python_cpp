for _ in range(int(input())):
    A = list(map(int, input().rstrip()))
    idx = 0
    for i in range(len(A) - 1, 0, -1):
        if A[i] > A[i - 1]:
            if i == len(A) - 1:
                idx = len(A) - 2
            else:
                idx = i - 1
            break

    a, b = A[:idx], A[idx:]

    if not a or not b:
        print("BIGGEST")
    else:
        b.sort()
        for i in b:
            if i > A[idx]:
                a.append(b.pop(b.index(i)))
                a.extend(b)
                break

        print(''.join(map(str, a)))
