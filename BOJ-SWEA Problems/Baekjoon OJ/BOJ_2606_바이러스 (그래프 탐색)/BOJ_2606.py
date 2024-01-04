import sys
from collections import deque
sys.stdin = open('input.txt')

# input 값 입력 받기
N = int(input())
M = int(input())

# 필요한 변수들 생성하기
network = [0] * (N+1)       # 간선 정보를 담을 network 리스트 생성
infection = [0] * (N+1)     # 바이러스 여부를 담을 infection 리스트 생성
que = deque()

# network 리스트에 간선 정보 입력하기 (양방향 다 입력)
for _ in range(M):
    A, B = map(int, input().split())
    if network[A] == 0:
        network[A] = [B]
    else:
        network[A].append(B)

    if network[B] == 0:
        network[B] = [A]
    else:
        network[B].append(A)

# que에 1번 담기
que.append(1)

# while 문을 이용해 감염 여부 찾기
while que:
    num = que.popleft()
    infection[num] = 1

    if network[num] != 0:                                   # 연결된 컴퓨터가 있는 경우,
        for n in network[num]:                                  # 연결된 컴퓨터 번호 순회
            if (n not in que) and (infection[n] == 0):              # 연결된 컴퓨터 번호가 큐에 없거나 아직 감염이 안되었으면
                que.append(n)                                           # -> 큐에 해당 컴퓨터 번호 넣기

# 결과 출력
print(sum(infection) - 1)       # 바이러스가 걸린 컴퓨터 개수에서 1번 컴퓨터 자신은 제외