import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input값 입력 받기
N, M, V = map(int, input().split())
nodes = [[0] * (N+1) for _ in range(N+1)]   # 노드 정보를 담을 매트릭스 생성

for _ in range(M):
    A, B = map(int, input().split())    # 노드 입력갑을 받은 후,
    nodes[A][B] = nodes[B][A] = 1       # 연결된 노드는 1로 표기


# DFS (깊이 우선 탐색) 계산하기
def DFS(V):
    visited[V] = 1
    print(V, end=' ')
    for j in range(1, N+1):
        if (nodes[V][j] == 1) and (visited[j] == 0):
            DFS(j)


# BFS (너비 우선 탐색) 계산하기
def BFS(V):
    que = deque([V])        # 큐 생성 및 첫번째 노드 값 넣기
    visited[V] = 1          # 시작점은 방문 표기

    while que:
        num = que.popleft()
        print(num, end=' ')
        for j in range(1, N+1):        # 큐에서 꺼낸 노드와 연결된 노드 숫자를 모두 찾아서 큐에 담기
            if (nodes[num][j] == 1) and (visited[j] == 0):
                que.append(j)
                visited[j] = 1


# 결과 출력
visited = [0] * (N+1)   # 방문 이력을 담을 visited 리스트 생성
DFS(V)
print()
visited = [0] * (N+1)   # 방문 이력을 담을 visited 리스트 생성
BFS(V)