from itertools import permutations
N = int(input())
lst = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
for _ in range(N):
    num, s, b = map(int, input().split())
    num = list(str(num))
    remove_cnt = 0
    for i in range(len(num)):
        s_cnt, b_cnt = 0, 0
        i -= remove_cnt

        for j in range(3):
            num[j] = int(num[j])
            if num[j] in lst[i]:
                if j == lst[i].index(num[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            remove_cnt += 1
print(len(lst))