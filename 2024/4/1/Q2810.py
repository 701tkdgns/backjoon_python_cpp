N = int(input())
SL = input()
cnt = SL.count('LL')
if cnt <= 1:
    print(N)
else:
    print(N - cnt + 1)
