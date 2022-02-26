import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    n, p = map(int, input().split())
    num_mat = [list(map(int, input().split())) for _ in range(n)]


    kill_max = 0    # 가장 큰 바이러스 제거수를 담을 kill_max변수 0으로 지정
    for i in range(n):
        for j in range(n):

            # 상하좌우의 경우
            di = [-1, 1, 0, 0]          # 델타 i (상, 하, 좌, 우)
            dj = [0, 0, -1, 1]          # 델타 j (상, 하, 좌, 우)

            kill_num = num_mat[i][j]    # 각 중앙원소별 바이러스 제거수를 담을 kill_num변수를 중앙원소값으로 지정
            for k in range(4):
                for l in range(1, p+1):
                    ni = i + (di[k]*l)  # 중앙원소의 상하좌우 i값
                    nj = j + (dj[k]*l)  # 중앙원소의 상하좌우 j값
                    if 0 <= ni < n and 0 <= nj < n:
                        kill_num += num_mat[ni][nj]     # 상하좌우에 위치한 값을 kill_num변수에 누적

            if kill_num > kill_max:     # 이번 kill_num값이 최대값보다 높으면 kill_max 갱신
                kill_max = kill_num

            # X자 대각선의 경우
            di = [-1, -1, 1, 1]         # 델타 i (좌상, 우상, 좌하, 우하)
            dj = [-1, 1, -1, 1]         # 델타 j (좌상, 우상, 좌하, 우하)

            kill_num = num_mat[i][j]    # 각 중앙원소별 바이러스 제거수를 담을 kill_num변수를 중앙원소값으로 지정
            for k in range(4):
                for l in range(1, p+1):
                    ni = i + (di[k]*l)  # 중앙원소의 대각선 i값
                    nj = j + (dj[k]*l)  # 중앙원소의 대각선 j값
                    if 0 <= ni < n and 0 <= nj < n:
                        kill_num += num_mat[ni][nj]     # X자 대각선에 위치한 값을 kill_num변수에 누적

            if kill_num > kill_max:     # 이번 kill_num값이 최대값보다 높으면 kill_max 갱신
                kill_max = kill_num


    # 결과 출력
    print(f'#{tc} {kill_max}')