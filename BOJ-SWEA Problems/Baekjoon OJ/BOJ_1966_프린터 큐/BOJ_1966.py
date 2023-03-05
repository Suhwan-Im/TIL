import sys
from collections import deque
sys.stdin = open('input.txt')

# input 값 입력 받기
T = int(input())    # 테스트 케이스 수

# for문을 이용해 테스트케이스별 정답 구하기
for _ in range(T):
    N, M = map(int, input().split())
    que = deque(map(int, input().split()))

    count = 0       # 몇 번째로 인쇄되는지를 확인할 count 변수 생성
    while True:                     # while문을 이용해 정답 구하기
        if que[0] == max(que):          # 만약 첫번째 인쇄물이 가장 중요도가 높은 경우,
            count += 1                      # -> count 변수 1 증가
            if M == 0:                      # 선택한 문서가 제일 앞에 있는 경우,
                print(count)                    # -> count 출력 후 반복문 종료
                break
            else:                           # 만약 선택한 문서가 뒤쪽에 있는 경우,
                M -= 1                          # -> M값 1 감소
                que.popleft()                   # 첫번째 인쇄물 제거

        else:                           # 가장 중요도가 높은 인쇄물이 뒤에 있는 경우
            que.append(que.popleft())       # -> 첫번째 인쇄물을 맨 뒤로 이동
            if M > 0:                       # 만약 선택한 문서가 뒤쪽에 있는 경우,
                M -= 1                          # -> M값 1 감소
            else:                           # 선택한 문서가 제일 앞에 있는 경우,
                M = len(que) - 1                # -> M값을 인덱스 맨 뒤로 설정