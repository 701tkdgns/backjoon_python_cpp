N = int(input())
lst = []
for i in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

val = 0
lst.sort(key=lambda x: x[0])

for i in range(N):
    sub_lst = []
    for j in range(N):
        if i != j and lst[i][1] == lst[j][1]:
            sub_lst.append(abs(lst[i][0]-lst[j][0]))
    val += min(sub_lst)
print(val)