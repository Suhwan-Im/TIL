import sys
from collections import deque
sys.stdin = open('input.txt')

# 테스트 케이스
T = int(input())

for _ in range(T):
    # input 값 입력 받기
    M, N, K = map(int, input().split())

    farm = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        j, i = map(int, input().split())
        farm[i][j] = 1

    # 상하좌우 인덱스
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    # 전체 범위를 순회하면서 배추(1)가 있는 기점에서 que를 이용해 상하좌우로 이웃된 모든 배추를 0으로 바꾸고, count 수를 누적해가기 
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                que = deque()
                que.append([i, j])
                count += 1

                while que:
                    ci, cj = que.popleft()

                    for k in range(4):
                        ni = ci + di[k]
                        nj = cj + dj[k]

                        if (0 <= ni < N) and (0 <= nj < M) and (farm[ni][nj] == 1):
                            farm[ni][nj] = 0
                            que.append([ni, nj])

    print(count)

    ### check_mat 라는 farm과 같은 크기의 매트릭스를 만든 경우 -> 시간초과
    #
    # farm = [[0] * M for _ in range(N)]
    # check_mat = [[0] * M for _ in range(N)]
    # que_cabb = deque()
    # que_temp = deque()
    # count = 0
    #
    # for _ in range(K):
    #     j, i = map(int, input().split())
    #     farm[i][j] = 1
    #     que_cabb.append([i, j])
    #
    # # 상하좌우 인덱스
    # di = [-1, 1, 0, 0]
    # dj = [0, 0, -1, 1]
    #
    # while que_cabb:
    #     count += 1
    #     a, b = que_cabb.popleft()
    #     que_temp.append([a, b])
    #
    #     while que_temp:
    #         ci, cj = que_temp.popleft()
    #         check_mat[ci][cj] = 1
    #
    #         for k in range(4):
    #             ni = ci + di[k]
    #             nj = cj + dj[k]
    #
    #             if (0 <= ni < N) and (0 <= nj < M) and (farm[ni][nj] == 1) and (check_mat[ni][nj] == 0):
    #                 que_temp.append([ni, nj])
    #
    #                 if [ni, nj] in que_cabb:
    #                     que_cabb.remove([ni, nj])
    #
    # print(count)