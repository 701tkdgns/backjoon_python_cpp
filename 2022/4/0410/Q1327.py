for _ in range(int(input())):
    a, b = input().split()
    A = list(a)
    B = list(b)
    if len(A) != len(B):
        print(-1)
    else:
        cnt = 0
        j = 1
        for i in range(1, len(A)):
            if B[i] == 'a':
                while A[j] != 'a':
                    j += 1
                cnt += abs(i-j)
                j += 1
        print(cnt)
