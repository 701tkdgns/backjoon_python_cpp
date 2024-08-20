d_body, d_tail = input().split()
m_body, m_tail = input().split()
lst = [d_body, d_tail, m_body, m_tail]
# lst.sort()
bird = []
for i in range(4):
    for j in range(4):
        if [lst[i], lst[j]] not in bird:
            bird.append([lst[i], lst[j]])
bird.sort(key=lambda x:(x[0], x[1]))
for body, tail in bird:
    print(body, tail)