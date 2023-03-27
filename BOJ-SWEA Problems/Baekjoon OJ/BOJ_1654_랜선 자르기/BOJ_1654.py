import sys
sys.stdin = open('input.txt')

# input 값 입력 받기
K, N = map(int, input().split())
cable_list = [int(input()) for _ in range(K)]

max = sum(cable_list) // N      # 초기 최대값
min = 1                         # 초기 최소값

# while문을 이용해서 최대값 구하기
while max >= min:
    cnt = 0                     # 랜선 개수를 담을 cnt 변수 0으로 생성
    mid = (max + min) // 2      # 중앙값 계산
    for cable in cable_list:    # 케이블 리스트를 돌며 케이블 개수 누적하기
        cnt += cable // mid

    if cnt >= N:                # 만약 현재 케이블 개수가 요구개수 이상인 경우,
        min = mid + 1           # -> 최소값을 중앙값 + 1로 변경
    else:                       # 케이블 개수가 요구개수보다 미달인 경우,
        max = mid - 1           # -> 최대값을 중앙값 - 1로 변경

# 결과 출력
print(max)
