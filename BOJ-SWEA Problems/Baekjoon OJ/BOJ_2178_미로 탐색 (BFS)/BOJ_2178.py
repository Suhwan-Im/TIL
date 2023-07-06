import sys
from collections import deque
sys.stdin = open('input.txt')

# input 값 입력 받기
N, M = map(int, input().split())
num_mat = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]       # 미로와 같은 크기의 visited 리스트 생성

si, sj = 1, 1           # 시작 인덱스 si, sj 설정
count = 1               # 미로 찾기 최소 턴 수를 구할 count 변수 1로 생성
que = deque()           # 빈 큐 생성
que.append([si, sj, count])    # 큐에 시작 인덱스와 턴 수 삽입
visited[0][0] = 1       # 시작 인덱스는 방문으로 표시

# 4방향 인덱스 di, dj 설정
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# while문을 이용해 미로 탐색하기 (BFS 활용)
while que:
    ci, cj, cnt = que.popleft()

    if ci == N and cj == M:     # 현재 좌표가 도착 위치인 경우,
        print(cnt)              # -> 턴 수를 출력하고
        break                   # -> while문 종료

    count = cnt + 1         # 턴 수는 기존 턴수에서 1 증가

    for k in range(4):      # 현재 위치 기준으로 인접한 4방향 탐색
        ni = ci + di[k]
        nj = cj + dj[k]

        if (1 <= ni <= N) and (1 <= nj <= M) and (visited[ni-1][nj-1] == 0) and (num_mat[ni-1][nj-1] == 1):    # 만약 새 좌표가 범위내에 있고 아직 방문하지 않은 길인 경우,
            visited[ni-1][nj-1] = 1             # -> visited 리스트의 같은 위치를 1로 갱신
            que.append([ni, nj, count])         # -> que에 해당 좌표와 턴 수 삽입