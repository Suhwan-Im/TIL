import sys
sys.stdin = open('input.txt')


# DFS 함수 정의
def DFS(n):
    global ans
    if n == N:      # DFS 함수가 N회 반복 된 경우 (퀸을 모든 줄에 놓은 경우)
        ans += 1    # -> ans 값을 1 증가
        return      # -> DFS 함수 반환
    for j in range(N):      # for 문을 이용해 각 행별 퀸을 놓을 수 있는 위치 찾기
        if check(n, j):         # check 함수를 이용해 퀸을 놓을 수 있는 경우,
            visited[n][j] = 1   # -> visited 매트릭스에 현재 위치를 1로 갱신
            DFS(n+1)            # -> DFS 함수 적용
            visited[n][j] = 0   # -> visited 매트릭스를 원상태로 복구

# check 함수 정의
def check(si, sj):
    # 위쪽 방향에 퀸이 놓여있는지 확인
    for i in range(si-1, -1, -1):
        if visited[i][sj] == 1:     # 퀸이 있는 경우
            return 0                # -> 0(False)을 반환

    # 좌측 대각선 위쪽에 퀸이 놓여있는지 확인
    i, j = si-1, sj-1               # 새로운 좌표를 좌측상단으로 지정
    while i >= 0 and j >= 0:        # 새로운 좌표가 범위 안에 있는동안 while 문 반목
        if visited[i][j] == 1:      # 퀸이 있는 경우
            return 0                # -> 0(False)을 반환
        i, j = i-1, j-1             # 다음 좌측상단 칸으로 진행

    # 우측 대각선 위쪽에 퀸이 놓여있는지 확인
    i, j = si-1, sj+1               # 새로운 좌표를 우측상단으로 지정
    while i >= 0 and j < N:         # 새로운 좌표가 범위 안에 있는동안 while 문 반목
        if visited[i][j] == 1:      # 퀸이 있는 경우
            return 0                # -> 0(False)을 반환
        i, j = i-1, j+1             # 다음 우측상단 칸으로 진행

    # 위쪽으로 걸리는 퀸이 없는 경우
    return 1                        # -> 1(True)을 반환

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]   # N x N 크기의 visited 매트릭스 생성

    ans = 0     # 모든 경우의 수를 담을 ans 변수를 0으로 생성
    DFS(0)      # DFS 함수를 이용해서 경우의 수 구하기

    # 결과 출력
    print(f'#{tc} {ans}')