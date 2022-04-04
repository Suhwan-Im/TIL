import sys
sys.stdin = open('input.txt')


# BFS 함수 구현하기
def BFS(si, sj, fi, fj):
    que = []                                    # 큐 생성
    visited = [[1e100] * N for _ in range(N)]   # visited 매트릭스 생성
    que.append((si, si))                        # 큐에 시작 좌표를 삽입
    visited[si][sj] = num_mat[si][sj]           # visited 매트릭스상의 현재 좌표에 복구시간을 넣기

    while que:
        ci, cj = que.pop(0)                     # 큐의 첫번째 원소를 꺼내서 ci, cj로 저장
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):       # 상하좌우 4방향 탐색
            ni, nj = ci + di, cj + dj                           # 새로운 좌표의 값을 ni, nj에 넣기
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] > visited[ci][cj] + num_mat[ni][nj]: # 새로운 좌표가 범위내이고 새로운 visited 값이 최저인 경우,
                que.append((ni, nj))                                    # 큐에 새로운 좌표 삽입
                visited[ni][nj] = visited[ci][cj] + num_mat[ni][nj]     # visited 리스트에 최소 값 갱신
    return visited[fi][fj]                      # 종료 좌표의 값을 반환

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat = [list(map(int, input())) for _ in range(N)]

    ans = BFS(0, 0, N-1, N-1)       # BFS(시작 i, 시작 j, 종료 i, 종료 j)

    # 결과 출력
    print(f'#{tc} {ans}')