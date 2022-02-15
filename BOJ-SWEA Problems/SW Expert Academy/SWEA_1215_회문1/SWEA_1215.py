import sys
sys.stdin = open('input.txt')

# 회문을 판별하는 함수 정의
def palindrome(str):
    pali = 0
    while len(str) >= 1:
        if len(str) == 1:
            pali = 1
            break
        elif str[0] == str[-1]:
            str = str[1:-1]
            pali = 1
        else:
            pali = 0
            break
    return pali

# 테스트 케이스를 통한 코드 실행
T = 10
for tc in range(1, T + 1):
    N = int(input())  # 회문의 길이
    # 리스트내 for문을 이용해 8x8의 매트릭스 생성
    str_mat = [list(map(str, input())) for _ in range(8)]

    cnt = 0

    # 가로단어 회문 갯수 구하기
    for i in range(8):
        for j in range(8-N+1):
            word_row = []
            for k in range(N):
                word_row.append(str_mat[i][j+k])

            word_r = ''.join(word_row)

            if palindrome(word_r):
                cnt += 1


    # 세로단어 회문 갯수 구하기
    for i in range(8-N+1):
        for j in range(8):
            word_col = []
            for k in range(N):
                word_col.append(str_mat[i+k][j])

            word_c = ''.join(word_col)

            if palindrome(word_c):
                cnt += 1


    # 결과 출력
    print(f'#{tc} {cnt}')