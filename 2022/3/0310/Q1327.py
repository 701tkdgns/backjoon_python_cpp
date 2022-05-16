from collections import deque


n, k = map(int, input().split())
lst = list(map(int, input().split()))
visitedS = set(''.join(lst))
dq = deque([[''.join(lst), 0]])
ans = -1

while dq:
    word, cnt = dq.popleft()
    tmp = list(word)

    if tmp == sorted(tmp):
        ans = cnt
        break

    for i in range(n-k+1):
        new = list(tmp)
        target = new[i:i+k]
        target.reverse()
        for j in range(k):
            new[i+j] = target[j]
        newWord = ''.join()
        if newWord not in visitedS:
            visitedS.add(newWord)
            dq.append([newWord,cnt+1])