import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
M, N = map(int, input().split())
storage = []
for _ in range(N):
    row = list(map(int, input().split()))
    storage.append(row)

step = 0
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 익은 토마토 좌표를 큐에 넣기
que = deque()
matures = []
for i in range(N):
    for j in range(M):
        if storage[i][j] == 1:
            matures.append([i, j])
que.append(matures)

# while 문을 이용해 최소날짜 구하기 (deque를 활용한 BFS)
while que:
    new_matures = []
    index_set = que.popleft()
    for index in index_set:
        ci, cj = index[0], index[1]

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]

            if (0 <= ni < N) and (0 <= nj < M) and storage[ni][nj] == 0:
                new_matures.append([ni, nj])
                storage[ni][nj] = 1

    if len(new_matures) > 0:
        que.append(new_matures)
        step += 1

# 익지 않은 토마토가 있는지 조회하고 그렇지 않은 경우 최소일 수 출력
immature_switch = 0

for s in storage:
    if 0 in s:
        print(-1)
        immature_switch = 1
        break

if immature_switch == 0:
    print(step)