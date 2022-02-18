import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            num_kill = 0
            for k in range(M):
                for l in range(M):
                    num_kill += num_mat[i+k][j+l]

            if num_kill > max_kill:
                max_kill = num_kill


    # 결과 출력
    print(f'#{tc} {max_kill}')