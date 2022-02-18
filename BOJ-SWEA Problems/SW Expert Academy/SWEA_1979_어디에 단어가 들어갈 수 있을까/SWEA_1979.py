import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    # 최종 갯수 변수 cnt를 0으로 지정
    cnt = 0

    # 가로줄 찾기
    for i in range(N):
        for j in range(N - K + 1):
            word_cnt = 0
            for k in range(K):
                word_cnt += num_mat[i][j + k]
            # if문 조건을 만족하면 최종개수에 1 추가 (j+k 범위가 시작점 또는 끝점 포함이거나 이전 및 직후가 0일 경우)
            if (j == 0 or num_mat[i][j - 1] == 0) and (j + K == N or num_mat[i][j + K] == 0) and word_cnt == K:
                cnt += 1

    # 세로줄 찾기
    for i in range(N - K + 1):
        for j in range(N):
            word_cnt = 0
            for k in range(K):
                word_cnt += num_mat[i + k][j]
            # if문 조건을 만족하면 최종개수에 1 추가 (i+k 범위가 시작점 또는 끝점 포함이거나 이전 및 직후가 0일 경우)
            if (i == 0 or num_mat[i - 1][j] == 0) and (i + K == N or num_mat[i + K][j] == 0) and word_cnt == K:
                cnt += 1

    # 결과 출력
    print(f'#{tc} {cnt}')