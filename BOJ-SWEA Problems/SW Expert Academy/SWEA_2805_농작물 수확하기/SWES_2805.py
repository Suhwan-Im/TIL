import sys
sys.stdin = open('input.txt')


# input값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat = [list(map(int, input())) for _ in range(N)]

    tot = 0

    for i in range(N//2):
        for j in range(N//2 - i, N//2 + i+1):
            tot += num_mat[i][j]

    for k in range(N//2, N):
        for l in range(k - N//2, N - (k - N//2)):
            tot += num_mat[k][l]

    # 결과 출력
    print(f'#{tc} {tot}')
