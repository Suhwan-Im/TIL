import sys
sys.stdin = open('input.txt')


# my_abs 함수 정의
def my_abs(num):
    if num < 0:
        return -num
    else:
        return num


# 테스트 케이스를 통한 코드 실행
T = int(input())
for tc in range(1, T + 1):
    num_mat = [list(map(int, input().split())) for _ in range(9)]

    # status 변수 정의 (1: 정답 / 0: 오답)
    status = 1

    # 접근 방식:
    # 가로줄, 세로줄, 3x3의 유형별로 검증
    # 각 검증시 1이 9개 있는 check_list를 이용해 (인덱스+1)의 숫자가 스도쿠에 있으면 1리스트에서 1씩 차감
    # 9개의 숫자를 모두 검증한 이후 check_list의 절대값의 합을 구해서 0이 아닌경우 오답으로 처리 (status 변수를 0으로 바꿈)

    # 가로줄 검증
    for i in range(len(num_mat)):
        check_list = [1] * 9
        for num in num_mat[i]:
            for c_i in range(len(check_list)):
                if c_i + 1 == num:
                    check_list[c_i] -= 1
        check_val = 0
        for check in check_list:
            check_val += my_abs(check)

        if check_val != 0:
            status = 0

    # 세로줄 검증
    for j in range(len(num_mat[0])):
        check_list = [1] * 9
        for i in range(len(num_mat)):
            for c_i in range(len(check_list)):
                if c_i + 1 == num_mat[i][j]:
                    check_list[c_i] -= 1
        check_val = 0
        for check in check_list:
            check_val += my_abs(check)

        if check_val != 0:
            status = 0

    # 3x3 박스 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check_list = [1] * 9
            for k in range(3):
                for l in range(3):
                    for c_i in range(len(check_list)):
                        if c_i + 1 == num_mat[i + k][j + l]:
                            check_list[c_i] -= 1
            check_val = 0
            for check in check_list:
                check_val += my_abs(check)

            if check_val != 0:
                status = 0

    # 결과 출력
    print(f'#{tc} {status}')