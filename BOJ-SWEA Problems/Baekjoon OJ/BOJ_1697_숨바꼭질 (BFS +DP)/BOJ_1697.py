import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N, K = map(int, input().split())
turn_list = [0] * 100001    # 각 위치의 최단시간을 담을 turn_list 생성
que = deque()       # 큐 생성
que.append(N)       # 큐에 N값 삽입

# while문을 이용해 (bfs + dp) 최단 시간 구하기
while que:
    n = que.popleft()

    # n값이 K와 같다면 현재 위치의 시간값 출력 & while문 종료
    if n == K:
        print(turn_list[n])
        break

    # 현재 n값 기준으로 -1, +1, *2 위치에 대해 시간 누적하기
    for new_n in [n-1, n+1, n*2]:
        if (0 <= new_n <= 100000) and (turn_list[new_n] == 0):  # 만약 new_n이 범위내에 있고, 아직 방문하지 않은 위치라면
            que.append(new_n)                                       # -> que에 new_n값 넣기
            turn_list[new_n] = turn_list[n] + 1                     # -> turn_list 상의 새로운 위치에 (현재위치 시간 + 1) 값 넣기