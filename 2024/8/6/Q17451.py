import math

# 두 숫자의 최소 공배수(LCM)를 계산하는 함수
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# 입력 처리
N = int(input())
lst = list(map(int, input().split()))

# 초기 최소 속도 설정
current_lcm = lst[0]

# 각 속도를 순회하며 최소 공배수를 업데이트
for i in range(1, N):
    current_lcm = lcm(current_lcm, lst[i])

print(current_lcm)
