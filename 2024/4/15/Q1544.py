from collections import deque


def chk_word(W1, W2):
    if len(W1) != len(W2):
        return W2
    dq = deque(W2)
    for i in range(len(W2)):
        dq.rotate(1)
        t = ''.join(dq)
        if t == W1:
            return W1
    return ''.join(dq)


n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
for i in range(n):
    for j in range(i, n):
        if lst[i] != lst[j]:
            lst[j] = chk_word(lst[i], lst[j])
print(len(set(lst)))