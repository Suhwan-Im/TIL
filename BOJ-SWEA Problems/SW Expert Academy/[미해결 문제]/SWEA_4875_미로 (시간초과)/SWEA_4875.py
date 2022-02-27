import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_mat = [list(map(int, input())) for _ in range(N)]

    # 출구 찾기 (첫줄에서 값이 3인 인덱스)
    curr_i = 0
    curr_j = 0
    for idx in range(N):
        if num_mat[0][idx] == 3:
            curr_j = idx

    # 출구에서부터 역으로 0 따라가기
    di = [-1, 1, 0, 0]      # 델타 i (상하좌우)
    dj = [0, 0, -1, 1]      # 델타 j (상하좌우)
    stack = []              # 빈 스택
    rlt = 0                 # 결과를 반환할 rlt 변수
    stop = 0                # while문 종료에 쓰일 stop 변수

    while stop != 1:
        num_mat[curr_i][curr_j] = 4             # 지나간 길 표시
        for k in range(4):                      # 상하좌우 길 탐색
            ni = curr_i + di[k]                 # 새로운 i 인덱스
            nj = curr_j + dj[k]                 # 새로운 j 인덱스
            if 0 <= ni < N and 0 <= nj < N:
                if num_mat[ni][nj] == 0:                # 새로 탐색한 칸이 0일 경우
                    stack.append([curr_i, curr_j])      # -> stack에 기존 인덱스 push
                    curr_i, curr_j = ni, nj             # -> 새로운 인덱스를 curr_i, curr_j에 업데이트
                    break
                elif num_mat[ni][nj] == 2:              # 새로 탐색한 칸이 2일 경우
                    rlt = 1                             # -> 결과 변수를 1로 지정
                    stop = 1                            # -> while문을 종료할 stop변수 1로 지정
                    break
                elif k == 3 and (num_mat[ni][nj] == 1 or num_mat[ni][nj] == 4):     # 4방향 모두 0또는 2가 없는 경우
                    back = stack.pop()                                              # -> 이전 인덱스를 stack에서 pop
                    curr_i, curr_j = back[0], back[1]                               # -> 이전 인덱스를 현재인덱스로 지정 (되돌아가기)
                    if len(stack) == 0:                                             # -> 만약 stack이 0일 경우 (시작점까지 되돌아온 경우)
                        stop = 1                                                    # -> while문을 종료할 stop변수 1로 지정
                        break
            elif k == 3:                                # 4방향 모두 0 또는 2가 없는 경우 (마지막 검색이 배열 밖인경우)
                back = stack.pop()                      # -> 이전 인덱스를 stack에서 pop
                curr_i, curr_j = back[0], back[1]       # -> 이전 인덱스를 현재인덱스로 지정 (되돌아가기)
                if len(stack) == 0:                     # -> 만약 stack이 0일 경우 (시작점까지 되돌아온 경우)
                    stop = 1                            # -> while문을 종료할 stop변수 1로 지정
                    break

    # 결과 출력
    print(f'#{tc} {rlt}')