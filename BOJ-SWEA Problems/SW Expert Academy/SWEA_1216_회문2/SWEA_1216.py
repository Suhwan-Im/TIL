import sys
sys.stdin = open('input.txt')


# 함수 정의
def max_pali(str_mat):
    # 회문의 길이
    for l in range(100, 0, -1):
        # 가로단어 회문 갯수 구하기
        for i in range(100):
            for j in range(100-l+1):
                word_row = str_mat[i][j:j+l]

                if word_row == word_row[::-1]:
                    return l

        # 세로단어 회문 갯수 구하기
        for i in range(100-l+1):
            for j in range(100):
                word_col = []
                for k in range(l):
                    word_col.append(str_mat[i+k][j])

                if word_col == word_col[::-1]:
                    return l


T = 10
for tc in range(1, T + 1):
    N = int(input())  # 테스트 케이스 숫자
    # 리스트내 for문을 이용해 100x100의 매트릭스 생성
    str_mat = [list(map(str, input())) for _ in range(100)]

    # max_pali 함수를 이용해 계산하기
    rlt = max_pali(str_mat)

    # 결과 출력
    print(f'#{tc} {rlt}')