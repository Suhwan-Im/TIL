import sys
sys.stdin = open('input.txt')

from collections import deque
# BFS 함수 정의
def BFS(N, M):
    visited = [0] * 1000001
    que = deque()       # 빈 큐 생성 (런타임 해결을 위해 deque 모듈 사용)
    que.append((N, 0))  # 큐에 N값과 카운트 횟수를 삽입

    while que:                          # 큐에 원소가 있는 동안 반복문 진행
        num, cnt = que.popleft()        # 큐에서 첫번째 숫자를 꺼내서 num 변수에 저장
        if num == M:                    # 만약 숫자가 M값과 같은 경우,
            return cnt                  # -> cnt 변수를 반환
        cnt += 1                        # 연산횟수 1 증가
        # 숫자가 M값과 다른 경우, 새로 계산한 숫자가 미방문이고 범위내일때,
        if 0 < num+1 <= 1000000 and visited[num+1] == 0:
            visited[num+1] = 1          # -> visited 리스트에 새값을 방문 표시
            que.append((num+1, cnt))    # -> 현재 숫자에 +1 연산한 값을 sub_que에 저장
        if 0 < num-1 <= 1000000 and visited[num-1] == 0:
            visited[num-1] = 1          # -> visited 리스트에 새값을 방문 표시
            que.append((num-1, cnt))    # -> 현재 숫자에 -1 연산한 값을 sub_que에 저장
        if 0 < num*2 <= 1000000 and visited[num*2] == 0:
            visited[num*2] = 1          # -> visited 리스트에 새값을 방문 표시
            que.append((num*2, cnt))    # -> 현재 숫자에 *2 연산한 값을 sub_que에 저장
        if 0 < num-10 <= 1000000 and visited[num-10] == 0:
            visited[num-10] = 1         # -> visited 리스트에 새값을 방문 표시
            que.append((num-10, cnt))   # -> 현재 숫자에 -10 연산한 값을 sub_que에 저장

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # BFS 함수를 이용해 최소 연산횟수 구하기
    ans = BFS(N, M)     # BFS(시작값, 결과값)

    # 결과 출력
    print(f'#{tc} {ans}')