def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1  # 하나의 기지국이 커버할 수 있는 아파트 수
    start = 1  # 아파트 시작 지점

    for station in stations:
        # 현재 기지국이 커버할 수 있는 첫 아파트 이전 구간을 계산
        end = station - w - 1
        if start <= end:
            # 커버리지 밖의 구간 길이를 계산하고 필요한 기지국 수를 추가
            answer += (end - start + 1 + coverage - 1) // coverage
        start = station + w + 1  # 다음 기지국의 커버리지 이후로 시작 지점을 이동

    # 마지막 기지국 이후로 남은 구간 처리
    if start <= n:
        answer += (n - start + 1 + coverage - 1) // coverage

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/12979?language=python3