import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    num_mat = [list(map(int, input().split())) for _ in range(Q)]

    box_list = [0] * N

    for i in range(1, Q + 1):
        for j in range(num_mat[i - 1][0] - 1, num_mat[i - 1][1]):
            box_list[j] = i

    # 결과 출력
    print(f'#{tc}', *box_list[:])