import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 문자열을 str_mat에 매트리스 형식으로 입력
    str_mat = []
    for i in range(N):
        str_mat.append(list(map(str, input())))

    # 가로줄 회문 찾기
    for i in range(N):
        for j in range(N-M+1):
            word_row = []
            for k in range(M):
                word_row.append(str_mat[i][j + k])

            word_r = ''.join(word_row)

            if word_r == word_r[::-1]:
                rlt = word_r

    # 세로줄 회문 찾기
    for i in range(N-M+1):
        for j in range(N):
            word_col = []
            for k in range(M):
                word_col.append(str_mat[i + k][j])

            word_c = ''.join(word_col)

            if word_c == word_c[::-1]:
                rlt = word_c


    # 결과 출력
    print(f'#{tc} {rlt}')