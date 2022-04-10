import sys
sys.stdin = open('input.txt')


# PRIM 함수 정의
def PRIM(r, V):
    visited = [0]*(V+1)     # visited 리스트 생성
    key = [1e100]*(V+1)     # key 리스트를 큰 값으로 생성
    key[r] = 0              # 시작정점의 key 값을 0으로 갱신
    for _ in range(V):
        u = 0               # 현재 인덱스를 표시할 u 변수를 0으로 생성
        minV = 1e100        # 가중치의 최소 값을 넣을 minV 변수를 큰 수로 생성
        for i in range(V+1):
            if visited[i] == 0 and key[i] < minV:   # 방문한적이 없고 현재값이 최저인 경우,
                u = i                               # u 값을 현재 인덱스로 갱신
                minV = key[i]                       # 현재값을 최저값으로 변경
        visited[u] = 1                              # visited 리스트에 현재 위치를 방문으로 표시

        for v in range(V+1):
            if visited[v] == 0 and adjM[u][v] > 0:  # 방문한적이 없고 인접행렬에 원소가 있는 경우
                key[v] = min(key[v], adjM[u][v])    # visited에 포함된 비용과 기존 비용을 비교
    return sum(key)         # 최소 가중치의 합을 반환

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]

    adjM = [[0]*(V+1) for _ in range(V+1)]  # 인접 행렬 생성
    adjL = [[] for _ in range((V+1))]       # 인접 리스트 생성
    for node in nodes:                      # for 문을 이용해 인접 행렬에 트리정보 넣기
        adjM[node[0]][node[1]] = node[2]
        adjM[node[1]][node[0]] = node[2]

    ans = PRIM(0, V)        # PRIM 알고리즘으로 최소신장트리 가중치의 합 구하기

    # 결과 출력
    print(f'#{tc} {ans}')