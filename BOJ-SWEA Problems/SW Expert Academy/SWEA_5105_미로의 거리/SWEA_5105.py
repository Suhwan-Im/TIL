import sys
sys.stdin = open('input.txt')

from collections import deque


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat = [list(map(int, input())) for _ in range(N)]
    sol_mat = [[0] * N for _ in range(N)]

    # 출발점 인덱스 찾기
    for i in range(N):
        for j in range(N):
            if num_mat[i][j] == 2:
                start_idx = [i, j]

    # 4방향 인덱스 설정 (상하좌우)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 큐 생성
    que = deque()
    que.append(start_idx)

    cnt = 0     # cnt 변수 0으로 생성해서 미로찾기 실패시 0 반환
    # while문 이용해서 미로 찾기
    while que:
        i, j = que.popleft()
        for k in range(4):  # 현재위치의 4방향을 ni, nj 인덱스로 설정
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and sol_mat[ni][nj] == 0:    # 새로운 인덱스가 미로범위 내이고, 이미 지나온 길이 아닐때
                if num_mat[ni][nj] == 0:                # 미로의 길(0)인 경우,
                    que.append([ni, nj])                    # ->  큐에 새로운 인덱스 추가하기
                    sol_mat[ni][nj] = sol_mat[i][j] + 1     # -> 지나온 칸 수 누적하기
                elif num_mat[ni][nj] == 3:              # 출구(3)를 찾은 경우,
                    cnt = sol_mat[i][j]                     # -> cnt 변수에 지나온 칸 수 넣기


    # 결과 출력
    print(f'#{tc} {cnt} {sol_mat}')