import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0] * (N+1) for _ in range(N+1)]

    # 초기 돌 배치
    board[N//2][N//2] = board[N//2+1][N//2+1] = 2
    board[N//2][N//2+1] = board[N//2+1][N//2] = 1

    for _ in range(M):
        sj, si, d = map(int, input().split())
        board[si][sj] = d
        for di, dj in ((-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1), (0,-1), (0,1)):
            s = []
            for k in range(1, N):
                ni, nj = si + di*k, sj + dj*k
                if 1 <= ni <= N and 1 <= nj <= N:
                    if board[ni][nj] == 0:
                        break
                    elif board[ni][nj] == d:
                        for ci, cj in s:
                            board[ci][cj] = d
                        break
                    else:
                        s.append((ni, nj))
                else:
                    break

    bcnt, wcnt = 0, 0
    for lst in board:
        bcnt += lst.count(1)
        wcnt += lst.count(2)

    # 결과 출력
    print(f'#{tc} {bcnt} {wcnt}')