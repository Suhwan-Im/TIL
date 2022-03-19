import sys
sys.stdin = open('input.txt')


# BFS 함수 정의
def BFS(N, M, R, C, L):

    que = []
    que.append((R, C))
    visited[R][C] = 1

    while que:
        i, j = que.pop(0)

        # 파이프 타입에 대한 모든 경우의 수 별로 인덱스를 que에 삽입하고 visited 리스트에 숫자 누적해가기
        if num_mat[i][j] == 1:
            if 0 <= (i-1) < N and (num_mat[i-1][j] in [1, 2, 5, 6]) and visited[i-1][j] == 0:
                que.append((i-1, j))
                visited[i-1][j] = visited[i][j] + 1
            if 0 <= (i+1) < N and (num_mat[i+1][j] in [1, 2, 4, 7]) and visited[i+1][j] == 0:
                que.append((i+1, j))
                visited[i+1][j] = visited[i][j] + 1
            if 0 <= (j-1) < M and (num_mat[i][j-1] in [1, 3, 4, 5]) and visited[i][j-1] == 0:
                que.append((i, j-1))
                visited[i][j-1] = visited[i][j] + 1
            if 0 <= (j+1) < M and (num_mat[i][j+1] in [1, 3, 6, 7]) and visited[i][j+1] == 0:
                que.append((i, j+1))
                visited[i][j+1] = visited[i][j] + 1
        elif num_mat[i][j] == 2:
            if 0 <= (i-1) < N and (num_mat[i-1][j] in [1, 2, 5, 6]) and visited[i-1][j] == 0:
                que.append((i-1, j))
                visited[i-1][j] = visited[i][j] + 1
            if 0 <= (i+1) < N and (num_mat[i+1][j] in [1, 2, 4, 7]) and visited[i+1][j] == 0:
                que.append((i+1, j))
                visited[i+1][j] = visited[i][j] + 1
        elif num_mat[i][j] == 3:
            if 0 <= (j-1) < M and (num_mat[i][j-1] in [1, 3, 4, 5]) and visited[i][j-1] == 0:
                que.append((i, j-1))
                visited[i][j-1] = visited[i][j] + 1
            if 0 <= (j+1) < M and (num_mat[i][j+1] in [1, 3, 6, 7]) and visited[i][j+1] == 0:
                que.append((i, j+1))
                visited[i][j+1] = visited[i][j] + 1
        elif num_mat[i][j] == 4:
            if 0 <= (i-1) < N and (num_mat[i-1][j] in [1, 2, 5, 6]) and visited[i-1][j] == 0:
                que.append((i-1, j))
                visited[i-1][j] = visited[i][j] + 1
            if 0 <= (j+1) < M and (num_mat[i][j+1] in [1, 3, 6, 7]) and visited[i][j+1] == 0:
                que.append((i, j+1))
                visited[i][j+1] = visited[i][j] + 1
        elif num_mat[i][j] == 5:
            if 0 <= (i+1) < N and (num_mat[i+1][j] in [1, 2, 4, 7]) and visited[i+1][j] == 0:
                que.append((i+1, j))
                visited[i+1][j] = visited[i][j] + 1
            if 0 <= (j+1) < M and (num_mat[i][j+1] in [1, 3, 6, 7]) and visited[i][j+1] == 0:
                que.append((i, j+1))
                visited[i][j+1] = visited[i][j] + 1
        elif num_mat[i][j] == 6:
            if 0 <= (i+1) < N and (num_mat[i+1][j] in [1, 2, 4, 7]) and visited[i+1][j] == 0:
                que.append((i+1, j))
                visited[i+1][j] = visited[i][j] + 1
            if 0 <= (j-1) < M and (num_mat[i][j-1] in [1, 3, 4, 5]) and visited[i][j-1] == 0:
                que.append((i, j-1))
                visited[i][j-1] = visited[i][j] + 1
        elif num_mat[i][j] == 7:
            if 0 <= (i-1) < N and (num_mat[i-1][j] in [1, 2, 5, 6]) and visited[i-1][j] == 0:
                que.append((i-1, j))
                visited[i-1][j] = visited[i][j] + 1
            if 0 <= (j-1) < M and (num_mat[i][j-1] in [1, 3, 4, 5]) and visited[i][j-1] == 0:
                que.append((i, j-1))
                visited[i][j-1] = visited[i][j] + 1

# input값 입력받기
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    num_mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    # BFS함수 이용하기
    BFS(N, M, R, C, L)

    total = 0   # 탈주범이 L시간 동안 위치할 수 있는 지점의 개수를 담을 total 변수 0 으로 생성
    # 이중 for 문을 이용해 visited 매트릭스의 모든 원소를 검사
    for visit in visited:
        for idx in visit:
            if idx != 0 and idx <= L:   # 원소가 0초과 L이하 인 경우
                total += 1              # total 값 1씩 증가시키기

    # 결과 출력
    print(f'#{tc} {total}')