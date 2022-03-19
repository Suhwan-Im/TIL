import sys
sys.stdin = open('input.txt')


# BFS 함수 정의
def BFS(si, sj):
    que = []        # 빈 큐 생성
    stack = []      # 빈 스택 생성

    que.append((si, sj))    # 큐에 입력 좌표 넣기
    visited[si][sj] = 1     # 해당 좌표를 visited 매트릭스에서 1로 갱신
    stack.append(num_mat[si][sj])   # 스택에 해당 좌표에 할당되어있는 숫자를 넣기

    while que:
        ci, cj = que.pop(0)     # 큐에서 좌표 꺼내기
        for di, dj in ([-1, 0], [1, 0], [0, -1], [0, 1]):   # 상하좌우를 검색하기
            ni, nj = ci + di, cj + dj                       # ni와 nj 변수에 di, dj를 더해서 인접좌표 구하기
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and abs(num_mat[ci][cj]-num_mat[ni][nj]) == 1:
                # 만약 인접좌표가 범위내에 존재하고, 해당 좌표에 방문한 적이 없고, 실제좌표와 인접좌표의 할당숫자의 차가 1일때,
                que.append((ni,nj))             # -> 큐에 인접좌표 넣기
                visited[ni][nj] = 1             # -> 인접좌표를 visited 매트릭스에서 1로 갱신
                stack.append(num_mat[ni][nj])   # -> 스택에 인접좌표에 할당되어있는 숫자를 넣기
    return min(stack), len(stack)       # 스택의 최소숫자(처음 출발할 방번호)와 스택의 길이(몇개의 방을 경유하는지)를 반환

# input값 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)] # num_mat과 같은 크기의 visited 매트릭스 생성
    num = N*N   # 조건을 만족하는 수 중의 최소값을 넣을 num 변수를 최댓값(N*N)으로 생성
    cnt = 0     # 조건을 만족하는 최대 연속갯수를 넣을 cnt 변수를 0 으로 생성
    
    # for 문을 이용해 배열의 모든 수를 BFS 함수로 검증
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                tnum, tcnt = BFS(i, j)  # BFS 함수에 넣어서 tnum과 tcnt 반환받기
                if (cnt < tcnt) or (cnt == tcnt and num > tnum):    # 만약 tcnt가 최고값이거나, 동등하면서 tnum이 최저값일때
                    cnt = tcnt                                      # -> cnt 변수에 tcnt 값을 갱신
                    num = tnum                                      # -> num 변수에 tnum 값을 갱신

    # 결과 출력
    print(f'#{tc} {num} {cnt}')