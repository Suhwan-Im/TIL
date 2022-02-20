import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    # 90도 돌린 매트릭스
    num_mat_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            num_mat_90[i][j] = num_mat[N - j - 1][i]

    # 180도 돌린 매트릭스
    num_mat_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            num_mat_180[i][j] = num_mat_90[N - j - 1][i]

    # 270도 돌린 매트릭스
    num_mat_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            num_mat_270[i][j] = num_mat_180[N - j - 1][i]

    # 결과 출력
    print(f'#{tc}')

    for i in range(N):
        print(''.join(map(str, num_mat_90[i])), ''.join(map(str, num_mat_180[i])), ''.join(map(str, num_mat_270[i])))