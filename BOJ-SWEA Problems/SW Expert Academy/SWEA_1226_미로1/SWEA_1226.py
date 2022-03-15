import sys
sys.stdin = open('input.txt')


T = 10
for _ in range(1, T+1):
    N = 16
    tc = int(input())
    num_mat = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]   # 미로와 같은 크기의 visited 매트릭스 생성

    start_idx = [1, 1]      # 시작 인덱스 지정
    que = []                # 빈 큐 생성
    que.append(start_idx)   # 큐에 시작 인덱스 삽입

    # 4방향 인덱스 di, dj 설정
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    rlt = 0 # rlt 변수 0으로 지정 (미로의 길이 없는 경우 0 리턴)
    # while문을 통해 미로 탐색
    while que:
        idx = que.pop(0)        # que의 첫번째 원소를 꺼내서 idx 변수에 담기
        for k in range(4):      # 현재 위치에서 4방향 각각 탐색
            ni = idx[0] + di[k]
            nj = idx[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:    # 해당 위치가 미로 범위내에 있고, visited 매트릭스 상에서 0일때
                if num_mat[ni][nj] == 0:        # 해당 위치가 미로에서 길(0)인 경우,
                    visited[ni][nj] = 1         # -> visited 매트릭스에 해당위치를 1로 갱신
                    que.append([ni, nj])        # -> 해당 인덱스를 큐에 삽입
                elif num_mat[ni][nj] == 3:      # 해당 위치가 미로에서 출구(3)인 경우,
                    rlt = 1                     # -> rlt 변수에 1을 넣고
                    break                       # -> while문 종료

    # 결과 출력
    print(f'#{tc} {rlt}')