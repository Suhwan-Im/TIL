import sys
sys.stdin = open('input.txt')


# max_len 함수 정의 (매트릭스 내에서 가장 긴 리스트의 길이 반환)
def max_len(str_mat):
    max_len = 0
    for str in str_mat:
        length = len(str)
        if max_len < length:
            max_len = length
    return max_len


# 테스트 케이스를 통한 코드 실행
T = int(input())
for tc in range(1, T + 1):
    str_mat = [list(map(str, input())) for _ in range(5)]

    # max_len 함수를 이용해 빈 매트릭스를 만들기 위한 N값 구하기
    N = max_len(str_mat)
    # Nx5의 'none'값이 들어있는 매트릭스 생성
    base_mat = [['none'] * N for _ in range(5)]

    # for문을 이용해 str_mat의 값을 base_mat에 적용하기
    for i in range(len(str_mat)):
        for j in range(len(str_mat[i])):
            base_mat[i][j] = str_mat[i][j]

    # for문과 if문을 이용해 'none'값이 아닌 값들을 세로순으로 정렬하기
    rlt = ''
    for j in range(len(base_mat[0])):
        for i in range(len(base_mat)):
            if base_mat[i][j] != 'none':
                rlt += base_mat[i][j]

    # 결과 출력
    print(f'#{tc} {rlt}')