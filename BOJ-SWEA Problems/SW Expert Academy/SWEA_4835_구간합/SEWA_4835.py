import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    # 숫자합의 최대값과 최소값 변수 임의 지정
    num_min = 1000000
    num_max = 0

    # for문을 이용해 각 구간별 합 구하기
    for i in range(N - M + 1):
        num_sum = 0
        for j in range(M):
            num_sum += num_list[i + j]

        # if문 두개를 이용해 최대값과 최소값 반영
        if num_sum > num_max:
            num_max = num_sum
        if num_sum < num_min:
            num_min = num_sum

    # 최대값과 최소값의 차이 계산
    diff = num_max - num_min

    # 결과 출력
    print(f'#{tc} {diff}')