import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    # 결과를 나타내는 rlt변수 0으로 지정
    rlt = 0

    # 칼로 자르는 가변구간 설정 (행과 열 모두 '0과 1 사이'부터 'N-1과 N 사이'들의 조합)
    for i in range(1, N):
        for j in range(1, N):

            # area 1 (좌상단 조각)
            sum_a1 = 0          # area 1 딸기 개수의 합을 저장할 sum_a1변수를 0으로 생성
            for a1_i in range(0, i):
                for a1_j in range(0, j):
                    sum_a1 += num_mat[a1_i][a1_j]   # (0,0) 부터 칼로 자른 범위내의 모든 값을 sum_a1 변수에 누적

            # area 2 (우상단 조각)
            sum_a2 = 0
            for a2_i in range(0, i):
                for a2_j in range(j, N):
                    sum_a2 += num_mat[a2_i][a2_j]

            # area 3 (좌하단 조각)
            sum_a3 = 0
            for a3_i in range(i, N):
                for a3_j in range(0, j):
                    sum_a3 += num_mat[a3_i][a3_j]

            # area 4 (우하단 조각)
            sum_a4 = 0
            for a4_i in range(i, N):
                for a4_j in range(j, N):
                    sum_a4 += num_mat[a4_i][a4_j]

            # 모든 구역의 딸기 개수가 같은 경우 (결과값을 1로 변경)
            if sum_a1 == sum_a2 == sum_a3 == sum_a4:
                rlt = 1


    # 결과 출력
    print(f'#{tc} {rlt}')