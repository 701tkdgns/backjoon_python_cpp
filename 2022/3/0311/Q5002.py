import sys
n = int(sys.stdin.readline())
lst = list(sys.stdin.readline().strip())
m_cnt, w_cnt = 0, 0
res = 0
for i in range(len(lst)):
    # 남자 여자 차이가 N보다 작을 경우에는 바로 증가
    if abs(m_cnt-w_cnt) < n:
        if lst[i] == 'M':
            m_cnt += 1
        else:
            w_cnt += 1
        res += 1
    # 남자 여자 차이가 N일 경우
    else:
        if lst[i] == 'M':
            # 남자 차례에서 남자를 증가시켰을 때 차이가 N보다 작으면 남자 증가
            if abs(m_cnt + 1 - w_cnt) < n:
                m_cnt += 1
                res += 1
            else:
                # 남자가 많아서 여자를 증가시켜야 하는 경우
                # 현재 순서 다음에 여자이면 순서 바꿔서 여자를 입장
                if i + 1 < len(lst) and lst[i + 1] == 'W':
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    w_cnt += 1
                    res += 1
                else:
                    break
        else:
            # 여자 차례에서 여자를 증가시켰을 때 차이가 N보다 작으면
            if abs(w_cnt + 1 - m_cnt) < n:
                w_cnt += 1
                res += 1
            else:
                # 여자가 많아서 남자를 증가시켜야 하는 경우
                # 현재 순서 다음에 남자이면 순서 바꿔서 남자를 입장
                if i + 1 < len(lst) and lst[i+1] == 'M':
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    m_cnt += 1
                    res += 1
                # 순서 바꿔도 불가능하면 종료
                else:
                    break
print(res)
