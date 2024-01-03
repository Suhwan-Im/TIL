import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
ans_map = [ [-1] * M for _ in range(N)]

# 시작점 인덱스 찾기
si, sj = 0, 0
for i in range(N):
    for j in range(M):
        if map[i][j] == 0:      # 여기서 미리 0으로 설정해서 고립되어있는 0이 -1로 남는것 방지
            ans_map[i][j] = 0
        if map[i][j] == 2:      # 시작점 찾으면 si, sj 변수에 값 저장
            si = i
            sj = j

# 기본값 설정하기
distance = 0
que = deque()
que.append([[si, sj]])

# 4방향 index di, dj 생성 (상, 하, 좌, 우)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# while 문을 이용해 거리 누적하기
while que:
    index_list = que.popleft()
    new_index = []
    for index in index_list:
        ci, cj = index[0], index[1]

        # 현재 위치의 상태에 맞게 ans_map에 값 저장
        if map[ci][cj] == 0:
            ans_map[ci][cj] = 0
        else:
            ans_map[ci][cj] = distance

            # 상하좌우 탐색 후 유효하면 새로운 인덱스 저장
            for k in range(4):
                ni = ci + di[k]
                nj = cj + dj[k]

                if (0 <= ni < N) and (0 <= nj < M) and (ans_map[ni][nj] == -1):
                    if [ni, nj] not in new_index:
                        new_index.append([ni, nj])

    if len(new_index) > 0:      # new_index에 값이 있으면 que에 넣기
        que.append(new_index)

    distance += 1               # 거리 상수 1 증가

# 결과 출력
for line in ans_map:
    print(*line[:])