import sys
sys.stdin = open('input.txt')


# BFS 함수 정의
def BFS(N, M):
    que = []            # 빈 큐 생성
    que.append([N])     # 큐에 N값을 리스트 형식으로 넣기
    cnt = 0             # 연산 횟수를 담아줄 cnt 변수를 0으로 생성

    while que:                              # 큐에 원소가 있는 동안 반복문 진행
        num = que.pop(0)                    # 큐에서 첫번째 숫자리스트를 꺼내서 num 변수에 저장
        sub_que = []                        # 횟수별로 묶은 숫자 리스트를 저장할 sub_que 생성
        for i in range(len(num)):           # 큐에서 꺼낸 숫자리스트를 조회
            if num[i] - M > 10:             # 백트래킹 (해결 방안 구상중)
                 pass
            elif num[i] == M:               # 만약 숫자가 M값과 같은 경우,
                return cnt                  # -> cnt 변수를 반환
            else:                           # 숫자가 M값과 다른 경우,
                sub_que.append(num[i]+1)    # -> 현재 숫자에 +1 연산한 값을 sub_que에 저장
                sub_que.append(num[i]-1)    # -> 현재 숫자에 -1 연산한 값을 sub_que에 저장
                sub_que.append(num[i]*2)    # -> 현재 숫자에 *2 연산한 값을 sub_que에 저장
                sub_que.append(num[i]-10)   # -> 현재 숫자에 -10 연산한 값을 sub_que에 저장
        que.append(sub_que)                 # sub_que를 que에 누적
        cnt += 1                            # 연산횟수 1 증가

# input 값 입력받기
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # BFS 함수를 이용해 최소 연산횟수 구하기
    ans = BFS(N, M)     # BFS(시작값, 결과값)

    # 결과 출력
    print(f'#{tc} {ans}')