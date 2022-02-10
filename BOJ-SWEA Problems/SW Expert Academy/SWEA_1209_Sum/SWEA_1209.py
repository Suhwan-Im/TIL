import sys
sys.stdin = open('input.txt')


# line_sum_max 함수 정의
def line_sum_max(num_mat):
    # max_sum 변수 0으로 생성
    max_sum = 0

    # 가로줄 - 각 줄의 합 중 최대값을 max_sum에 저장
    for i in range(100):
        if sum(num_mat[i]) > max_sum:
            max_sum = sum(num_mat[i])

    # 세로줄 - 각 줄의 합 중 최대값을 max_sum에 저장
    for i in range(100):
        cur_sum = 0
        for j in range(100):
            cur_sum += num_mat[j][i]
        if cur_sum > max_sum:
            max_sum = cur_sum

    # 대각선 (좌상 -> 우하)
    cur_sum = 0
    for i in range(100):
        cur_sum += num_mat[i][i]
    if cur_sum > max_sum:
        max_sum = cur_sum

    # 대각선 (우상 -> 좌하)
    cur_sum = 0
    for i in range(100):
        cur_sum += num_mat[99-i][i]
    if cur_sum > max_sum:
        max_sum = cur_sum

    # 최대값 반환
    return max_sum


# 테스트 케이스를 통한 코드 실행
T = 10
for tc in range(1, T + 1):
    N = int(input()) # 테스트케이스 번호
    # 리스트내 for문을 이용해 100x100의 매트릭스 생성
    num_mat = [list(map(int, input().split())) for _ in range(100)]

    # line_sum_max 함수를 통해 결과값 계산
    rlt = line_sum_max(num_mat)

    print(f'#{N} {rlt}')