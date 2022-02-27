import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    blank_mat = [[0] * N for _ in range(N)]
    sub_list = []

    # 배열을 순회하면서 화학 물질 사각형 탐색하고 행&열 사이즈를 sub_list에 담기
    for i in range(N):
        for j in range(N):
            if num_mat[i][j] != 0 and blank_mat[i][j] == 0:
                cnt_col = 0
                cnt_row = 0
                while num_mat[i][j] != 0:
                    cnt_row += 1
                    i += 1
                i -= cnt_row
                while num_mat[i][j] != 0:
                    cnt_col += 1
                    j += 1
                j -= cnt_col
                sub_list.append([cnt_row, cnt_col])

                for sub_i in range(i, i + cnt_row):
                    for sub_j in range(j, j + cnt_col):
                        blank_mat[sub_i][sub_j] = 1

    # sub_list 정렬하기
    for i in range(len(sub_list)):
        for j in range(len(sub_list)-i-1):
            if sub_list[j][0] * sub_list[j][1] > sub_list[j+1][0] * sub_list[j+1][1]:
                sub_list[j], sub_list[j + 1] = sub_list[j + 1], sub_list[j]
            elif (sub_list[j][0] * sub_list[j][1] == sub_list[j+1][0] * sub_list[j+1][1]) and (sub_list[j][0] > sub_list[j+1][0]):
                sub_list[j], sub_list[j+1] = sub_list[j+1], sub_list[j]

    # fin_list에 순서대로 담기
    fin_list = []
    for sub in sub_list:
        for idx in range(2):
            fin_list.append(sub[idx])


    # 결과 출력
    print(f'#{tc} {len(sub_list)}', *fin_list[:])