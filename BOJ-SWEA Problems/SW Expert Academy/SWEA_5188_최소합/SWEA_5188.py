import sys
sys.stdin = open('input.txt')


# DFS 함수 정의
def DFS(S, G, ssum):
    global min_sum
    ci, cj = S                  # 시작 좌표를 ci, cj로 받기
    ssum += num_mat[ci][cj]     # ssum 변수에 해당 좌표의 값 누적하기
    if ssum < min_sum:          # 현재 합계가 전체 최소 합계보다 작은 경우
        if S == G:                  # 만약 해당좌표가 종료좌표와 같다면,
            min_sum = ssum          # -> 최소 합계를 ssum 값으로 갱신
            return                  # -> DFS 함수 종료

        if 0 <= ci+1 < N and 0 <= cj < N:     # 새로운 좌표가 범위내인 경우, (아래쪽)
            DFS((ci+1, cj), G, ssum)          # -> 새로운 좌표를 이용해 DFS 함수 다시 호출
        if 0 <= ci < N and 0 <= cj+1 < N:     # 새로운 좌표가 범위내인 경우, (오른쪽)
            DFS((ci, cj+1), G, ssum)          # -> 새로운 좌표를 이용해 DFS 함수 다시 호출

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]

    S, G = (0, 0), (N-1, N-1)       # 시작과 종료 좌표를 S, G 변수로 설정
    min_sum = 1e100                 # 최소 합계를 담을 min_sum 변수를 큰수로 생성
    ssum = 0                        # 각각의 경우의 합계를 누적할 ssum 변수를 0으로 생성

    # DFS 함수 이용 (시작좌표, 종료좌표, 누적값)
    DFS(S, G, ssum)

    # 결과 출력
    print(f'#{tc} {min_sum}')