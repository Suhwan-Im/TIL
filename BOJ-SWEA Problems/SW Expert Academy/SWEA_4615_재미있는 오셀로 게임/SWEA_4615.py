import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_mat = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * (N+1) for _ in range(N+1)]

    # 초기 돌 배치
    board[N//2][N//2] = 2
    board[N//2][N//2+1] = 1
    board[N//2+1][N//2] = 1
    board[N//2+1][N//2+1] = 2

    # 8방향 좌표 (좌측상단부터 우측하단까지 8개 방향)
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    # for 문을 이용해 돌을 하나씩 놓으며 규칙대로 뒤집어주기
    for turn in num_mat:
        ci, cj = turn[0], turn[1]                   # 현재 i와 j 좌표를 의미하는 ci, cj 변수에 해당 값 넣어주기
        board[ci][cj] = turn[2]                     # ci, cj 좌표에 돌 놓기

        for k in range(8):                          # for 문을 이용해 8방향 탐색하기
            ni = ci + di[k]                         # 새로운 i 좌표를 의미하는 ni 변수에 인접 i 값 넣기
            nj = cj + dj[k]                         # 새로운 j 좌표를 의미하는 nj 변수에 인접 j 값 넣기
            mult = 1                                # 새로운 좌표를 확장시킬때 사용할 mult 변수를 1로 생성
            while 1 <= ni <= N and 1 <= nj <= N:    # while 문을 이용해서 필요한 만큼 좌표를 확장시키며 탐색하기
                if board[ni][nj] == 0:              # 인접 좌표가 0인 경우,
                    break                           # -> 반복문 종료
                elif board[ni][nj] == turn[2]:      # 인접 좌표가 놓은 돌과 같은색의 돌인 경우,
                    ni = ni - di[k]                 # -> ni 좌표을 역방향으로 돌리기
                    nj = nj - dj[k]                 # -> nj 좌표를 역방향으로 돌리기
                    while 1 <= ni <= N and 1 <= nj <= N and board[ni][nj] != turn[2]:   # while 문을 이용해 처음 놓은 돌까지 돌아가기
                        board[ni][nj] = turn[2]     # 돌아가며 다른색의 돌을 모두 놓은돌의 색과 같게 지정해주기
                        ni = ni - di[k]             # ni 좌표를 역방향으로 1칸 진행
                        nj = nj - dj[k]             # nj 좌표를 역방향으로 1칸 진행
                    break
                else:                               # 인접 좌표가 놓은 돌과 다른색의 돌인 경우,
                    mult += 1                       # mult 변수 1 증가
                    ni = ci + di[k]*mult            # -> ni 좌표를 같은 방향으로 한칸 더 이동하기
                    nj = cj + dj[k]*mult            # -> nj 좌표를 같은 방향으로 한칸 더 이동하기

    cnt_1, cnt_2 = 0, 0             # 검정색과 흰색 돌의 개수를 담을 cnt_1, cnt_2 변수를 0으로 생성
    for b_list in board:            # 이중 for 문을 이용해 게임판 순회하기
        for b_num in b_list:
            if b_num == 1:          # 돌의 색이 1인 경우,
                cnt_1 += 1          # -> cnt_1 변수를 1 증가
            elif b_num == 2:        # 돌의 색이 2인 경우,
                cnt_2 += 1          # -> cnt_2 변수를 1 증가

    # 결과 출력
    print(f'#{tc} {cnt_1} {cnt_2}')