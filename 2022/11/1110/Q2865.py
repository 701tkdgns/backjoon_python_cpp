N, M, K = map(int, input().split()) # N : 인원 수, M : 장르, K : 본선 출전
score = [0.0 for _ in range(N)]
for _ in range(M):
    tmp = list(map(float, input().split()))
    for i in range(0, len(tmp), 2):
        if score[int(tmp[i])-1] < tmp[i+1]:
            score[int(tmp[i])-1] = tmp[i+1]
score.sort()
res = sum(score[len(score)-K:])
print(round(res, 1))