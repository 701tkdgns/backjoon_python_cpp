genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
answer = []
# {장르 : 총 재생 횟수}
playdic = {}
# {장르 : [ ( 플레이 횟수, 고유 번호 ) ] }
d = {}

for i in range(len(genres)):
    g = genres[i]
    p = plays[i]
    playdic[g] = playdic.get(g, 0) + p
    d[g] = d.get(g, []) + [(p, i)]
print(playdic)
print(d)
genreSort = sorted(playdic.items(), key=lambda x: x[1], reverse=True)
print(genreSort)
for g, totp in genreSort:
    d[g] = sorted(d[g], key=lambda x: (-x[0], x[1]))
    answer += [idx for (p, idx) in d[g][:2]]
    print(answer)
print(d)
print(answer)