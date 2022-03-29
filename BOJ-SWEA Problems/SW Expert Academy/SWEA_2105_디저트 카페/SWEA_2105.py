import sys
sys.stdin = open('input.txt')


# DFS 함수 정의 -- DFS(방향, i죄표, j좌표, visited, 개수)
def DFS(n, ci, cj, v, cnt):
    global si, sj, ans
    if n > 3:
        return
    if n == 3 and ci == si and cj == sj and ans < cnt:
        ans = cnt
        return
    # 직진하는 경우 or 방향을 바꾸는 경우
    for k in range(n, n+2):
        ni, nj = ci+di[k], cj+dj[k]
        if 0 <= ni < N and 0 <= nj < N and num_mat[ni][nj] not in v:
            DFS(k, ni, nj, v+[num_mat[ni][nj]], cnt+1)

# input 값 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat  = [list(map(int, input().split())) for _ in range(N)]

    di, dj = [1, 1, -1, -1, 1], [-1, 1, 1, -1, -1]      # 5번째 방향시 함수 종료를 위해 1번 방향을 마지막에 한번 더 기술

    ans = -1
    for si in range(N):
        for sj in range(N):
            DFS(0, si, sj, [], 0)       # DFS(시작방향, i죄표, j좌표, visited 빈리스트, 개수)

    # 결과 출력
    print(f'#{tc} {ans}')