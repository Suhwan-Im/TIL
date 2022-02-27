import sys
sys.stdin = open('input.txt')

# 접근 방법: 각 세로줄별로 내려가면서 1 이후에 2가 나오면 교착개수를 1 증가하고, 계속 내려가면서 같은 방식으로 교착개수 누적해가기
T = 10
for tc in range(1, T + 1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0         # 교착 개수를 누적할 cnt 변수 0으로 생성
    for j in range(0, N):
        status = 0  # 현재 상태를 나타내는 status 변수 0으로 생성 (0: 교착 가능한 자성체가 현재 없는 상태 / 1: N극 성질을 가지는 미교착 자성체가 이전에 있는 경우)
        for i in range(0, N):                           # 각 열별로 내려가면서 자성체를 검사
            if num_mat[i][j] == 1 and status == 0:      # status가 0일때, N극 성질을 가지는 자성체가 나타난 경우
                status = 1                              # -> status 변수를 1로 갱신
            elif num_mat[i][j] == 2 and status == 1:    # status가 1일때, S극 성질을 가지는 자성체가 나타난 경우
                status = 0                              # -> status 변수를 0으로 갱신
                cnt += 1                                # -> 교착 개수를 나타내는 cnt 변수를 1 증가 시키기
            else:                                       # 위의 조건이 아닌 경우
                pass                                    # -> 다음 칸으로 진행

    # 결과 출력
    print(f'#{tc} {cnt}')