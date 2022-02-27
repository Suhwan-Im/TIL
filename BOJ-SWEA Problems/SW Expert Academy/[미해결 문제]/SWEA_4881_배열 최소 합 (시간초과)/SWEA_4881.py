import sys
sys.stdin = open('input.txt')


# 순열을 구하는 perm 함수
def perm(i):
    if i == len(p):
        perm_list.append(p[:])      # 순열을 perm_list에 담기
    else:
        for j in range(i, len(p)):
            p[i], p[j] = p[j], p[i]
            perm(i + 1)
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    p = [x for x in range(N)]   # 0에서 N-1까지의 숫자 리스트
    perm_list = []              # 순열을 담을 빈 리스트 생성
    perm(0)                     # 순열함수 이용해 순열 담기 (인덱스 0에서 시작)

    min_sum = 1e100
    for i in range(len(perm_list)):
        curr_sum = 0
        for idx in range(N):
            curr_sum += num_mat[idx][perm_list[i][idx]]

        if curr_sum < min_sum:
            min_sum = curr_sum


    # 결과 출력
    print(f'#{tc} {min_sum}')