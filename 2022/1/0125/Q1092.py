N = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
box = sorted(list(map(int, input().split())), reverse=True)
time = 0
cnt = 0
if max(box) > max(crane):
    print(-1)
else:
    while box:
        if not box:
            break
        for crane_idx in crane:
            for box_idx in box:
                if crane_idx >= box_idx:
                    box.remove(box_idx)
                    break
        time += 1
    print(time)


# 1. 각 크레인과 박스를 무게에 맞게 내림차순 정렬시켜준다.
# 2. 크레인이 들 수 있는 가장 무거운 박스를 옮긴다.
# 3. 모든 크레인에 대해서 해결했다면 시간을 1 올려준다.
# 4. 1 ~ 3의 과정을 반복한다.
