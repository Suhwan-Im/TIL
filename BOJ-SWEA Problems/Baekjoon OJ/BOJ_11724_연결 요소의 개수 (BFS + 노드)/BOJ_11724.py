import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input 값 입력 받기
N, M = map(int, input().split())
nodes = [0] * (N+1)         # 노드 정보를 담을 nodes 리스트 생성
visited = [1] + ([0] * N)   # 방문 노드 정보를 담을 visited 리스트 생성

# 노드 정보 채우기 (양방향 모두 채우기)
for _ in range(M):
    u, v = map(int, input().split())

    if nodes[u] == 0:
        nodes[u] = [v]
    else: #elif v not in nodes[u]:          * 'not in'을 넣으니 시간초과 (불필요한 단계 - 중복되는 간선이 없다고 이미 문제에 명시 됨)
        nodes[u].append(v)

    if nodes[v] == 0:
        nodes[v] = [u]
    else: #elif u not in nodes[v]:          * 심지어 두번이나 넣음..
        nodes[v].append(u)

# 필요한 변수 생성
que = deque()
count = 0       # 연결 요소의 총 개수를 담을 count 변수 생성

# 노드를 순회하며 연결 요소의 개수 구하기
for i in range(1, N+1):
    if visited[i] == 0:     # 아직 방문한적 없는 노드인 경우,
        visited[i] = 1          # -> 방문 정보 1로 갱신  
        if nodes[i] != 0:           # 해당 노드에 다른 간선 정보가 담겨있는 경우,
            que.extend(nodes[i])        # -> 큐에 간선 정보 담기 (* append가 아니라 extend를 쓰는 이유: 리스트로 감싸져있는 간선 정보에서 숫자들만 담기 위해)
            
            # 큐를 이용해 연결된 간선 모두 탐색하며 방문 정보 갱신해가기
            while que:
                num = que.popleft()
                if visited[num] == 0:
                    visited[num] = 1
                    for n in nodes[num]:
                        if (visited[n] == 0) and (n not in que):
                            que.append(n)

        count += 1  # 연결 요소 개수 누적하기

# 결과 출력
print(count)